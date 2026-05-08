from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any

from openai import OpenAI


DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")
LAB_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = LAB_DIR / "data"

SYSTEM_INSTRUCTIONS = """
You are a research assistant for an AI Agent learning lab.
Use web search for current public information.
Use file search for the local learning-lab corpus.
Do not pretend retrieved content is model memory.
When sources are available, cite them clearly in the answer.
""".strip()


def model_controls(model: str) -> dict[str, Any]:
    controls: dict[str, Any] = {}
    if model.startswith("gpt-5") or model.startswith("o"):
        controls["reasoning"] = {"effort": "low"}
    return controls


def dump_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def require_api_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set. Set it before running API-backed Lab 03.")


def corpus_files(paths: list[str]) -> list[Path]:
    if paths:
        files = [Path(path).expanduser().resolve() for path in paths]
    else:
        files = sorted(DEFAULT_DATA_DIR.glob("*.md"))

    missing = [path for path in files if not path.exists()]
    if missing:
        raise SystemExit(f"Missing corpus file(s): {', '.join(str(path) for path in missing)}")

    return files


def split_chunks(text: str) -> list[str]:
    chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
    return chunks or [text.strip()]


def query_terms(query: str) -> list[str]:
    ascii_terms = re.findall(r"[A-Za-z0-9_./-]+", query.lower())
    cjk_terms: list[str] = []

    for phrase in re.findall(r"[\u4e00-\u9fff]{2,}", query):
        cjk_terms.append(phrase)
        cjk_terms.extend(phrase[index : index + 2] for index in range(len(phrase) - 1))

    return ascii_terms + cjk_terms


def score_chunk(query: str, chunk: str) -> int:
    haystack = chunk.lower()
    terms = query_terms(query)
    score = sum(haystack.count(term.lower()) for term in terms)

    # Chinese queries often arrive as a phrase instead of tokenized words.
    compact_query = re.sub(r"\s+", "", query)
    compact_chunk = re.sub(r"\s+", "", chunk)
    if compact_query and compact_query in compact_chunk:
        score += 5

    return score


def local_search(query: str, files: list[Path], max_results: int) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []

    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        for index, chunk in enumerate(split_chunks(text), start=1):
            score = score_chunk(query, chunk)
            if score <= 0:
                continue
            candidates.append(
                {
                    "source": str(file_path),
                    "chunk": index,
                    "score": score,
                    "text": chunk,
                }
            )

    candidates.sort(key=lambda item: item["score"], reverse=True)
    return candidates[:max_results]


def upload_files_to_vector_store(client: OpenAI, files: list[Path], name: str) -> dict[str, Any]:
    uploaded_file_ids: list[str] = []

    for file_path in files:
        with file_path.open("rb") as file_handle:
            uploaded = client.files.create(file=file_handle, purpose="assistants")
        uploaded_file_ids.append(uploaded.id)

    vector_store = client.vector_stores.create(
        name=name,
        file_ids=uploaded_file_ids,
        expires_after={"anchor": "last_active_at", "days": 7},
        metadata={"lab": "03-tools-and-rag"},
    )

    vector_files = wait_for_vector_store_files(client, vector_store.id)
    return {
        "vector_store_id": vector_store.id,
        "uploaded_file_ids": uploaded_file_ids,
        "vector_store_files": vector_files,
    }


def wait_for_vector_store_files(
    client: OpenAI,
    vector_store_id: str,
    timeout_seconds: int = 90,
) -> list[dict[str, Any]]:
    deadline = time.monotonic() + timeout_seconds

    while True:
        files = list(client.vector_stores.files.list(vector_store_id, limit=100))
        summary = [
            {
                "id": file.id,
                "status": file.status,
                "last_error": (
                    file.last_error.model_dump()
                    if getattr(file.last_error, "model_dump", None)
                    else file.last_error
                ),
            }
            for file in files
        ]
        statuses = {file["status"] for file in summary}

        if statuses and statuses <= {"completed"}:
            return summary

        if "failed" in statuses or "cancelled" in statuses:
            raise SystemExit(dump_json({"vector_store_id": vector_store_id, "files": summary}))

        if time.monotonic() > deadline:
            raise SystemExit(
                dump_json(
                    {
                        "error": "Timed out waiting for vector store ingestion.",
                        "vector_store_id": vector_store_id,
                        "files": summary,
                    }
                )
            )

        time.sleep(2)


def output_item_types(response: Any) -> list[str]:
    return [getattr(item, "type", "unknown") for item in response.output]


def extract_url_citations(response: Any) -> list[dict[str, Any]]:
    citations: list[dict[str, Any]] = []

    for item in response.output:
        if getattr(item, "type", None) != "message":
            continue
        for content in getattr(item, "content", []):
            for annotation in getattr(content, "annotations", []):
                if getattr(annotation, "type", None) != "url_citation":
                    continue
                citations.append(
                    {
                        "title": getattr(annotation, "title", None),
                        "url": getattr(annotation, "url", None),
                        "start_index": getattr(annotation, "start_index", None),
                        "end_index": getattr(annotation, "end_index", None),
                    }
                )

    return citations


def extract_file_search_results(response: Any) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []

    for item in response.output:
        if getattr(item, "type", None) != "file_search_call":
            continue
        for result in getattr(item, "results", []) or []:
            if hasattr(result, "model_dump"):
                results.append(result.model_dump())
            else:
                results.append({"result": str(result)})

    return results


def run_research(args: argparse.Namespace) -> None:
    require_api_key()
    if not args.vector_store_id:
        raise SystemExit(
            "Run with --vector-store-id, or create one first with --prepare-vector-store."
        )

    client = OpenAI()
    response = client.responses.create(
        model=args.model,
        instructions=SYSTEM_INSTRUCTIONS,
        input=(
            "Research this topic using both public web sources and the local file-search corpus. "
            f"Topic: {args.topic}"
        ),
        tools=[
            {"type": "web_search", "search_context_size": args.search_context_size},
            {
                "type": "file_search",
                "vector_store_ids": [args.vector_store_id],
                "max_num_results": args.max_file_results,
            },
        ],
        include=[
            "file_search_call.results",
            "web_search_call.action.sources",
        ],
        max_tool_calls=4,
        parallel_tool_calls=False,
        text={"verbosity": "low"},
        **model_controls(args.model),
    )

    print(
        dump_json(
            {
                "model": args.model,
                "vector_store_id": args.vector_store_id,
                "output_item_types": output_item_types(response),
                "file_search_results": extract_file_search_results(response),
                "url_citations": extract_url_citations(response),
                "final_answer": response.output_text,
            }
        )
    )


def run_local_search(args: argparse.Namespace) -> None:
    files = corpus_files(args.files)
    print(
        dump_json(
            {
                "topic": args.topic,
                "mode": "local_search_only",
                "files": [str(path) for path in files],
                "results": local_search(args.topic, files, args.max_file_results),
            }
        )
    )


def prepare_vector_store(args: argparse.Namespace) -> None:
    require_api_key()
    files = corpus_files(args.files)
    client = OpenAI()
    result = upload_files_to_vector_store(client, files, args.vector_store_name)
    print(dump_json(result))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lab 03: Responses API web_search + file_search research assistant.",
    )
    parser.add_argument(
        "topic",
        nargs="?",
        default="OpenAI Agent 工具边界和检索能力应该怎么设计？",
        help="Research topic.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="OpenAI model id. Defaults to OPENAI_MODEL or gpt-5.5.",
    )
    parser.add_argument(
        "--file",
        dest="files",
        action="append",
        default=[],
        help="Local corpus file to upload/search. Can be repeated. Defaults to data/*.md.",
    )
    parser.add_argument(
        "--local-search-only",
        action="store_true",
        help="Search the local markdown corpus without calling the OpenAI API.",
    )
    parser.add_argument(
        "--prepare-vector-store",
        action="store_true",
        help="Upload local corpus files and create a vector store for file_search.",
    )
    parser.add_argument(
        "--vector-store-id",
        help="Existing vector store id to use with the file_search tool.",
    )
    parser.add_argument(
        "--vector-store-name",
        default="Lab 03 Tools and RAG Corpus",
        help="Name to use when creating a vector store.",
    )
    parser.add_argument(
        "--max-file-results",
        type=int,
        default=4,
        help="Maximum file_search results to request or local chunks to return.",
    )
    parser.add_argument(
        "--search-context-size",
        choices=["low", "medium", "high"],
        default="low",
        help="Web search context size.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.local_search_only:
        run_local_search(args)
        return

    if args.prepare_vector_store:
        prepare_vector_store(args)
        return

    run_research(args)


if __name__ == "__main__":
    main()
