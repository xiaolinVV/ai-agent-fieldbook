#!/usr/bin/env python3
"""Capture local assets for one learning video.

The script handles the mechanical part of the video-study-notes workflow:
download media/subtitles/metadata, clean transcript text, split transcript by
chapters, extract keyframes, and write a manifest for the note author.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


DEFAULT_MEDIA_ROOT = Path("local-media/youtube")
DEFAULT_ASR_MODEL_ROOT = Path("local-media/models/whisper.cpp")
DEFAULT_TOOL_ROOT = Path("local-media/tools")
DEFAULT_ASR_MODEL = "base-q5_1"
WHISPER_MODEL_URLS = {
    "tiny": "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.bin",
    "base": "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.bin",
    "base-q5_1": "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base-q5_1.bin",
    "small": "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin",
}
ASR_PROMPT = (
    "RAG, Retrieval-Augmented Generation, 检索增强生成, 分片, 索引, 向量, "
    "Embedding, 向量数据库, 召回, 重排, 生成, cosine similarity, vector database, "
    "knowledge base, LLM, ChatGPT, Claude, DeepSeek"
)
JS_RUNTIMES = ("deno", "node", "bun", "qjs", "quickjs")
LOCAL_WHISPER_CLI_PATHS = (
    DEFAULT_TOOL_ROOT / "whisper.cpp/build/bin/whisper-cli",
    DEFAULT_TOOL_ROOT / "whisper.cpp/build/bin/main",
    DEFAULT_TOOL_ROOT / "whisper.cpp/main",
    DEFAULT_TOOL_ROOT / "whisper.cpp/whisper-cli",
)
CODE_HOSTS = (
    "github.com",
    "gitlab.com",
    "gitee.com",
    "bitbucket.org",
    "huggingface.co",
    "sourceforge.net",
)
CODE_PATH_HINTS = (
    "github",
    "gitlab",
    "gitee",
    "repo",
    "repository",
    "source-code",
    "source_code",
    "code",
    "源码",
    "代码",
    "项目",
)
QUICKTIME_FORMAT = (
    "bv*[ext=mp4][vcodec^=avc1][height<=1080]+ba[ext=m4a][acodec^=mp4a]"
    "/b[ext=mp4][vcodec^=avc1][height<=1080]"
    "/bv*+ba/b"
)


def run(
    cmd: list[str],
    check: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, capture_output=True, text=True, errors="replace", env=env)
    if check and proc.returncode != 0:
        print("$ " + " ".join(cmd), file=sys.stderr)
        if proc.stdout.strip():
            print(proc.stdout[-4000:], file=sys.stderr)
        if proc.stderr.strip():
            print(proc.stderr[-4000:], file=sys.stderr)
        raise SystemExit(proc.returncode)
    return proc


def which(name: str) -> str | None:
    return shutil.which(name)


def whisper_cli_path(project_root: Path | str = Path(".")) -> str | None:
    for name in ("whisper-cli", "whisper.cpp"):
        path = which(name)
        if path:
            return path

    root = Path(project_root)
    for relative in LOCAL_WHISPER_CLI_PATHS:
        path = root / relative
        if path.is_file() and os.access(path, os.X_OK):
            return str(path)
    return None


def whisper_runtime_env(
    whisper_cli: str,
    base_env: dict[str, str] | None = None,
) -> dict[str, str]:
    env = dict(base_env or os.environ)
    path = Path(whisper_cli)
    if path.parent.name != "bin" or path.parent.parent.name != "build":
        return env

    build = path.parent.parent
    lib_dirs = [
        build / "src",
        build / "ggml/src",
    ]
    existing_dirs = [str(item) for item in lib_dirs if item.is_dir()]
    if not existing_dirs:
        return env

    key = "DYLD_LIBRARY_PATH" if sys.platform == "darwin" else "LD_LIBRARY_PATH"
    current = env.get(key)
    env[key] = ":".join(existing_dirs + ([current] if current else []))
    return env


def preflight() -> int:
    rows = []
    for name in ("yt-dlp", "ffmpeg", "ffprobe"):
        path = which(name)
        version = "missing"
        if path:
            arg = "-version" if name.startswith("ff") else "--version"
            proc = run([path, arg], check=False)
            version = (proc.stdout or proc.stderr).splitlines()[0]
        rows.append((name, path or "missing", version))
    whisper_path = whisper_cli_path()
    whisper_version = "missing"
    if whisper_path:
        proc = run([whisper_path, "--help"], check=False, env=whisper_runtime_env(whisper_path))
        whisper_version = "installed" if proc.returncode == 0 else "not runnable"
    rows.append(("whisper-cli", whisper_path or "missing", whisper_version))

    js = detect_js_runtime()
    proxy = detect_proxy("auto")
    default_model = asr_model_path(DEFAULT_ASR_MODEL, None)

    print("video-study-assets preflight")
    for name, path, version in rows:
        print(f"- {name}: {path} ({version})")
    print(f"- js runtime: {js[0] if js else 'missing'}")
    print(f"- proxy(auto): {proxy or 'none'}")
    print(f"- asr model({DEFAULT_ASR_MODEL}): {default_model if default_model.exists() else 'missing'}")

    missing = [name for name, path, _ in rows if path == "missing" and name != "whisper-cli"]
    if missing:
        print(f"Missing tools: {', '.join(missing)}", file=sys.stderr)
        return 1
    return 0


def detect_js_runtime() -> tuple[str, str] | None:
    for runtime in JS_RUNTIMES:
        path = which(runtime)
        if path:
            return runtime, path
    return None


def detect_proxy(value: str | None) -> str | None:
    if not value or value == "none":
        return None
    if value != "auto":
        return value

    for key in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "ALL_PROXY", "all_proxy"):
        proxy = os.environ.get(key)
        if proxy:
            return proxy

    if sys.platform != "darwin" or not which("scutil"):
        return None

    proc = run(["scutil", "--proxy"], check=False)
    if proc.returncode != 0:
        return None
    text = proc.stdout

    def field(name: str) -> str | None:
        match = re.search(rf"{re.escape(name)}\s*:\s*(.+)", text)
        return match.group(1).strip() if match else None

    https_enable = field("HTTPSEnable") == "1"
    http_enable = field("HTTPEnable") == "1"
    if https_enable and field("HTTPSProxy") and field("HTTPSPort"):
        return f"http://{field('HTTPSProxy')}:{field('HTTPSPort')}"
    if http_enable and field("HTTPProxy") and field("HTTPPort"):
        return f"http://{field('HTTPProxy')}:{field('HTTPPort')}"
    if field("SOCKSEnable") == "1" and field("SOCKSProxy") and field("SOCKSPort"):
        return f"socks5://{field('SOCKSProxy')}:{field('SOCKSPort')}"
    return None


def ytdlp_base(proxy: str | None) -> list[str]:
    cmd = ["yt-dlp", "--ignore-config"]
    if proxy:
        cmd.extend(["--proxy", proxy])
    js = detect_js_runtime()
    if js:
        cmd.extend(["--js-runtimes", f"{js[0]}:{js[1]}"])
    return cmd


def safe_slug(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:90] or "video-study"


def find_first(directory: Path, suffixes: tuple[str, ...]) -> Path | None:
    files = sorted(p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in suffixes)
    return files[0] if files else None


def find_video(directory: Path) -> Path | None:
    quicktime = sorted(directory.glob("*.quicktime.mp4"))
    if quicktime:
        return quicktime[0]
    return find_first(directory, (".mp4", ".mkv", ".webm", ".mov"))


def caption_tracks_available(info: dict[str, Any]) -> bool:
    return bool(info.get("subtitles") or info.get("automatic_captions"))


def local_asr_outputs_exist(subtitle: Path) -> bool:
    base = subtitle.with_suffix("")
    return Path(f"{base}.txt").exists() and Path(f"{base}.json").exists()


def subtitle_source(info: dict[str, Any], subtitle: Path | None) -> str:
    if not subtitle:
        return "missing"
    if local_asr_outputs_exist(subtitle):
        return "local ASR fallback or manually supplied subtitle"
    if caption_tracks_available(info):
        return "YouTube subtitle or automatic caption"
    return "local ASR fallback or manually supplied subtitle"


def parse_srt(path: Path) -> list[tuple[float, str]]:
    blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8", errors="replace").strip())
    segments: list[tuple[float, str]] = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 3:
            continue
        time_line = lines[1] if "-->" in lines[1] else lines[0]
        match = re.search(r"(\d\d):(\d\d):(\d\d),(\d\d\d)\s+-->", time_line)
        if not match:
            continue
        seconds = (
            int(match.group(1)) * 3600
            + int(match.group(2)) * 60
            + int(match.group(3))
            + int(match.group(4)) / 1000
        )
        text_lines = lines[2:] if time_line == lines[1] else lines[1:]
        text = clean_caption_text("".join(text_lines))
        if text:
            segments.append((seconds, text))
    return segments


def clean_caption_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fmt_time(seconds: float) -> str:
    seconds = max(0, int(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def load_info(directory: Path) -> dict[str, Any]:
    info_path = find_info_json(directory)
    if not info_path:
        return {}
    return json.loads(info_path.read_text(encoding="utf-8", errors="replace"))


def find_info_json(directory: Path) -> Path | None:
    files = sorted(directory.glob("*.info.json"))
    return files[0] if files else None


def extract_urls(text: str) -> list[str]:
    urls = re.findall(r"https?://[^\s<>)\]\"'）。，；、]+", text or "")
    cleaned: list[str] = []
    seen = set()
    for url in urls:
        url = url.rstrip(".,;，。；、")
        if url in seen:
            continue
        seen.add(url)
        cleaned.append(url)
    return cleaned


def collect_description_urls(info: dict[str, Any], source_url: str) -> list[str]:
    text = "\n".join(
        str(info.get(key) or "")
        for key in ("description", "webpage_url", "original_url")
    )
    urls = extract_urls(text)
    if source_url and source_url not in urls:
        urls.insert(0, source_url)
    return urls


def is_code_or_project_url(url: str) -> bool:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    if any(host == code_host or host.endswith(f".{code_host}") for code_host in CODE_HOSTS):
        return True
    return any(hint in path for hint in CODE_PATH_HINTS)


def transcript_mentions_code_repo(directory: Path) -> bool:
    transcript = directory / "transcript-clean.txt"
    if not transcript.exists():
        return False
    text = transcript.read_text(encoding="utf-8", errors="replace").lower()
    markers = ("github", "git hub", "仓库", "代码仓库", "源码", "repo", "repository")
    return any(marker in text for marker in markers)


def collect_comment_urls(comments: list[dict[str, Any]]) -> list[str]:
    urls: list[str] = []
    seen = set()
    for comment in comments:
        for url in extract_urls(str(comment.get("text") or "")):
            if url in seen:
                continue
            seen.add(url)
            urls.append(url)
    return urls


def write_comments_digest(directory: Path, comments: list[dict[str, Any]]) -> Path:
    pinned = [comment for comment in comments if comment.get("is_pinned")]
    uploader = [comment for comment in comments if comment.get("author_is_uploader")]
    url_comments = [
        comment for comment in comments
        if extract_urls(str(comment.get("text") or ""))
    ]
    top_comments = sorted(
        comments,
        key=lambda item: item.get("like_count") or 0,
        reverse=True,
    )[:20]

    def one_line(text: str, limit: int = 360) -> str:
        text = re.sub(r"\s+", " ", text or "").strip()
        if len(text) <= limit:
            return text
        return text[:limit].rstrip() + "..."

    lines = [
        "# Comments Digest",
        "",
        f"- total_comments: {len(comments)}",
        "",
        "## Pinned Comments",
        "",
    ]
    if pinned:
        for comment in pinned:
            lines.append(
                f"- {comment.get('author')}: {one_line(str(comment.get('text') or ''))}"
            )
    else:
        lines.append("- none found")

    lines.extend(["", "## URL Comments", ""])
    if url_comments:
        for comment in url_comments:
            urls = ", ".join(extract_urls(str(comment.get("text") or "")))
            lines.append(
                f"- {comment.get('author')} "
                f"(uploader={bool(comment.get('author_is_uploader'))}, likes={comment.get('like_count') or 0}): {urls}"
            )
    else:
        lines.append("- none found")

    lines.extend(["", "## Uploader Comments", ""])
    if uploader:
        for comment in uploader[:20]:
            lines.append(
                f"- likes={comment.get('like_count') or 0}, pinned={bool(comment.get('is_pinned'))}: "
                f"{one_line(str(comment.get('text') or ''))}"
            )
    else:
        lines.append("- none found")

    lines.extend(["", "## Top Comments By Likes", ""])
    for comment in top_comments:
        lines.append(
            f"- likes={comment.get('like_count') or 0}, "
            f"author={comment.get('author')}: {one_line(str(comment.get('text') or ''))}"
        )

    digest = directory / "comments-digest.md"
    digest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return digest


def fetch_comments(
    url: str,
    directory: Path,
    proxy: str | None,
    max_comments: int,
    force: bool,
) -> tuple[Path | None, Path | None, list[dict[str, Any]]]:
    comments_json = directory / "comments.json"
    if comments_json.exists() and not force:
        comments = json.loads(comments_json.read_text(encoding="utf-8", errors="replace"))
        digest = write_comments_digest(directory, comments)
        return comments_json, digest, comments

    cmd = ytdlp_base(proxy)
    cmd.extend([
        "--skip-download",
        "--write-comments",
        "--dump-single-json",
        "--extractor-args",
        f"youtube:max_comments={max_comments}",
        url,
    ])
    proc = run(cmd)
    data = json.loads(proc.stdout)
    comments = data.get("comments") or []
    comments_json.write_text(
        json.dumps(comments, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    digest = write_comments_digest(directory, comments)
    return comments_json, digest, comments


def choose_subtitle(directory: Path) -> Path | None:
    preferred_patterns = ("*.zh-Hans.srt", "*.zh-CN.srt", "*.zh.srt", "*.srt")
    for pattern in preferred_patterns:
        matches = sorted(directory.glob(pattern))
        if matches:
            return matches[0]
    return None


def asr_model_path(model_name: str, explicit_path: str | None) -> Path:
    if explicit_path:
        return Path(explicit_path)
    filename = f"ggml-{model_name}.bin"
    return DEFAULT_ASR_MODEL_ROOT / filename


def asr_output_base(directory: Path) -> Path | None:
    video = find_video(directory)
    if not video:
        return None
    name = video.name
    for suffix in (".quicktime.mp4", ".mp4", ".mkv", ".webm", ".mov"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    return directory / f"{name}.zh-Hans"


def download_asr_model(model_name: str, model_path: Path, proxy: str | None) -> None:
    url = WHISPER_MODEL_URLS.get(model_name)
    if not url:
        known = ", ".join(sorted(WHISPER_MODEL_URLS))
        raise SystemExit(f"Unknown ASR model '{model_name}'. Known models: {known}")

    model_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["curl", "-L", "--fail", "-C", "-", "-o", str(model_path), url]
    if proxy:
        cmd[1:1] = ["--proxy", proxy]
    run(cmd)


def run_asr_fallback(
    directory: Path,
    proxy: str | None,
    force: bool,
    model_name: str,
    model_path: Path,
    download_model: bool,
    threads: int,
    processors: int,
) -> Path | None:
    if choose_subtitle(directory) and not force:
        return choose_subtitle(directory)

    video = find_video(directory)
    output_base = asr_output_base(directory)
    if not video or not output_base:
        print("ASR fallback skipped: no local video found.", file=sys.stderr)
        return None

    whisper_cli = whisper_cli_path()
    if not whisper_cli:
        print(
            "ASR fallback skipped: whisper-cli is missing. "
            "Install whisper.cpp in PATH or build it under local-media/tools/whisper.cpp.",
            file=sys.stderr,
        )
        return None

    if not model_path.exists():
        if download_model:
            download_asr_model(model_name, model_path, proxy)
        else:
            print(
                f"ASR fallback skipped: model missing at {model_path}. "
                "Install/download it or pass --asr-download-model.",
                file=sys.stderr,
            )
            return None

    audio = directory / "audio-16k.wav"
    if force or not audio.exists():
        run([
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(video),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-c:a",
            "pcm_s16le",
            str(audio),
        ])

    run([
        whisper_cli,
        "-m",
        str(model_path),
        "-f",
        str(audio),
        "-l",
        "zh",
        "-t",
        str(threads),
        "-p",
        str(processors),
        "-bs",
        "1",
        "-bo",
        "1",
        "-osrt",
        "-ovtt",
        "-otxt",
        "-oj",
        "-of",
        str(output_base),
        "--prompt",
        ASR_PROMPT,
    ], env=whisper_runtime_env(whisper_cli))

    subtitle = Path(f"{output_base}.srt")
    return subtitle if subtitle.exists() else None


def write_transcripts(directory: Path, info: dict[str, Any]) -> tuple[Path | None, Path | None]:
    subtitle = choose_subtitle(directory)
    if not subtitle:
        return None, None

    segments = parse_srt(subtitle)
    clean_path = directory / "transcript-clean.txt"
    clean_path.write_text("\n".join(text for _, text in segments) + "\n", encoding="utf-8")

    chapter_path = directory / "chapter-transcript.md"
    chapters = info.get("chapters") or []
    lines = ["# Chapter Transcript", ""]
    if chapters:
        for chapter in chapters:
            start = float(chapter.get("start_time") or 0)
            end = float(chapter.get("end_time") or info.get("duration") or start)
            title = chapter.get("title") or "Untitled"
            body = "".join(text for t, text in segments if start <= t < end)
            lines.append(f"## {fmt_time(start)}-{fmt_time(end)} {title}")
            lines.append("")
            lines.append(body)
            lines.append("")
    else:
        lines.append("## Full Transcript")
        lines.append("")
        lines.append("".join(text for _, text in segments))
        lines.append("")
    chapter_path.write_text("\n".join(lines), encoding="utf-8")
    return clean_path, chapter_path


def frame_times(info: dict[str, Any]) -> list[float]:
    duration = float(info.get("duration") or 0)
    chapters = info.get("chapters") or []
    times: list[float] = []

    if chapters:
        for chapter in chapters:
            start = float(chapter.get("start_time") or 0)
            end = float(chapter.get("end_time") or duration or start + 1)
            span = max(1.0, end - start)
            times.append(min(end - 1, start + min(15, span * 0.35)))
            if span > 180:
                times.append(start + span * 0.65)
    elif duration:
        count = min(16, max(6, math.ceil(duration / 120)))
        times = [duration * (i + 1) / (count + 1) for i in range(count)]

    deduped: list[float] = []
    seen = set()
    for t in times:
        key = int(t)
        if key in seen or key < 0:
            continue
        seen.add(key)
        deduped.append(t)
    return deduped[:18]


def extract_frames(directory: Path, info: dict[str, Any], force: bool) -> Path | None:
    video = find_video(directory)
    if not video:
        return None

    frames_dir = directory / "frames"
    frames_dir.mkdir(exist_ok=True)
    existing = sorted(frames_dir.glob("frame-*.jpg"))
    if existing and not force:
        return frames_dir / "contact-keyframes.jpg" if (frames_dir / "contact-keyframes.jpg").exists() else None

    for old in frames_dir.glob("frame-*.jpg"):
        old.unlink()

    for t in frame_times(info):
        out = frames_dir / f"frame-{fmt_time(t).replace(':', '-')}.jpg"
        run([
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            fmt_time(t),
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(out),
        ])

    frames = sorted(frames_dir.glob("frame-*.jpg"))
    if not frames:
        return None

    rows = math.ceil(len(frames) / 3)
    contact = frames_dir / "contact-keyframes.jpg"
    run([
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-pattern_type",
        "glob",
        "-i",
        str(frames_dir / "frame-*.jpg"),
        "-vf",
        f"scale=640:-1,tile=3x{rows}",
        "-frames:v",
        "1",
        str(contact),
    ], check=False)
    return contact if contact.exists() else None


def download(url: str, directory: Path, proxy: str | None, force: bool) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    has_video = find_video(directory)
    has_info = find_first(directory, (".json",))
    if has_video and has_info and not force:
        return

    cmd = ytdlp_base(proxy)
    cmd.extend([
        "--no-playlist",
        "--no-progress",
        "-f",
        QUICKTIME_FORMAT,
        "--merge-output-format",
        "mp4",
        "-P",
        f"home:{directory}",
        "-o",
        "%(title)s [%(id)s].quicktime.%(ext)s",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        "zh-Hans,zh-CN,zh,zh-Hant,en",
        "--sub-format",
        "srt/vtt/best",
        "--convert-subs",
        "srt",
        "--write-info-json",
        "--write-thumbnail",
        "--embed-metadata",
        "--print",
        "after_move:filepath",
        url,
    ])
    run(cmd)


def write_manifest(
    directory: Path,
    url: str,
    slug: str,
    proxy: str | None,
    clean_path: Path | None,
    chapter_path: Path | None,
    contact: Path | None,
    comments_json: Path | None,
    comments_digest: Path | None,
    comments: list[dict[str, Any]],
) -> Path:
    info = load_info(directory)
    video = find_video(directory)
    subtitle = choose_subtitle(directory)
    info_path = find_info_json(directory)
    thumbnail = find_first(directory, (".webp", ".jpg", ".png"))
    description_urls = collect_description_urls(info, url)
    comment_urls = collect_comment_urls(comments)
    all_resource_urls = description_urls + [
        item for item in comment_urls if item not in description_urls
    ]
    code_urls = [item for item in all_resource_urls if is_code_or_project_url(item)]
    mentions_repo = transcript_mentions_code_repo(directory)

    upload_date = str(info.get("upload_date") or "")
    if len(upload_date) == 8:
        upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"

    lines = [
        "# Video Study Asset Manifest",
        "",
        f"- slug: `{slug}`",
        f"- url: {url}",
        f"- title: {info.get('title') or ''}",
        f"- channel: {info.get('channel') or info.get('uploader') or ''}",
        f"- upload_date: {upload_date}",
        f"- duration: {info.get('duration_string') or fmt_time(float(info.get('duration') or 0))}",
        f"- proxy: {proxy or 'none'}",
        f"- subtitle_source: {subtitle_source(info, subtitle)}",
        "",
        "## Local Assets",
        "",
        f"- video: `{video}`" if video else "- video: missing",
        f"- subtitle: `{subtitle}`" if subtitle else "- subtitle: missing",
        f"- info_json: `{info_path}`" if info_path else "- info_json: missing",
        f"- thumbnail: `{thumbnail}`" if thumbnail else "- thumbnail: missing",
        f"- transcript_clean: `{clean_path}`" if clean_path else "- transcript_clean: missing",
        f"- chapter_transcript: `{chapter_path}`" if chapter_path else "- chapter_transcript: missing",
        f"- keyframe_contact_sheet: `{contact}`" if contact else "- keyframe_contact_sheet: missing",
        f"- comments_json: `{comments_json}`" if comments_json else "- comments_json: missing",
        f"- comments_digest: `{comments_digest}`" if comments_digest else "- comments_digest: missing",
        "",
        "## Links From Description",
        "",
    ]
    if description_urls:
        lines.extend(f"- {item}" for item in description_urls)
    else:
        lines.append("- none found")

    lines.extend([
        "",
        "## Candidate Code Links",
        "",
    ])
    if code_urls:
        lines.extend(f"- {item}" for item in code_urls)
    elif mentions_repo:
        lines.append("- Transcript mentions a code repository/source code, but no concrete URL was found in video metadata or description.")
    else:
        lines.append("- none found")

    lines.extend([
        "",
        "## Chapters",
        "",
    ])
    for chapter in info.get("chapters") or []:
        start = float(chapter.get("start_time") or 0)
        end = float(chapter.get("end_time") or start)
        lines.append(f"- {fmt_time(start)}-{fmt_time(end)} {chapter.get('title') or 'Untitled'}")

    if not info.get("chapters"):
        lines.append("- No chapter metadata found.")

    lines.extend([
        "",
        "## Next Step",
        "",
        "Use this manifest plus `transcript-clean.txt`, `chapter-transcript.md`, comments, and keyframes to write a fieldbook note.",
    ])

    manifest = directory / "asset-manifest.md"
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return manifest


def capture(args: argparse.Namespace) -> int:
    media_root = Path(args.media_root)
    slug = args.slug or safe_slug(args.url)
    directory = media_root / slug
    proxy = detect_proxy(args.proxy)

    if not args.skip_download:
        download(args.url, directory, proxy, args.force_download)

    info = load_info(directory)
    subtitle = choose_subtitle(directory)
    if args.asr_fallback != "never" and (args.asr_fallback == "force" or not subtitle):
        run_asr_fallback(
            directory=directory,
            proxy=proxy,
            force=args.asr_fallback == "force",
            model_name=args.asr_model,
            model_path=asr_model_path(args.asr_model, args.asr_model_path),
            download_model=args.asr_download_model,
            threads=args.asr_threads,
            processors=args.asr_processors,
        )
    clean_path, chapter_path = write_transcripts(directory, info)
    contact = extract_frames(directory, info, args.force_frames)
    comments_json = None
    comments_digest = None
    comments: list[dict[str, Any]] = []
    if not args.skip_comments:
        comments_json, comments_digest, comments = fetch_comments(
            args.url,
            directory,
            proxy,
            args.comments_limit,
            args.force_comments,
        )
    manifest = write_manifest(
        directory,
        args.url,
        slug,
        proxy,
        clean_path,
        chapter_path,
        contact,
        comments_json,
        comments_digest,
        comments,
    )

    print(f"asset_dir: {directory.resolve()}")
    print(f"manifest: {manifest.resolve()}")
    if clean_path:
        print(f"transcript: {clean_path.resolve()}")
    if contact:
        print(f"keyframes: {contact.resolve()}")
    if comments_json:
        print(f"comments: {comments_json.resolve()}")
    if comments_digest:
        print(f"comments_digest: {comments_digest.resolve()}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capture learning video assets for notes.")
    sub = parser.add_subparsers(dest="command", required=True)

    pre = sub.add_parser("preflight")
    pre.set_defaults(func=lambda _args: preflight())

    cap = sub.add_parser("capture")
    cap.add_argument("url")
    cap.add_argument("--slug", help="Stable output directory name under media root.")
    cap.add_argument("--media-root", default=str(DEFAULT_MEDIA_ROOT))
    cap.add_argument("--proxy", default="auto", help="auto, none, or explicit proxy URL.")
    cap.add_argument("--skip-download", action="store_true")
    cap.add_argument("--skip-comments", action="store_true")
    cap.add_argument("--comments-limit", type=int, default=200)
    cap.add_argument("--force-download", action="store_true")
    cap.add_argument("--force-frames", action="store_true")
    cap.add_argument("--force-comments", action="store_true")
    cap.add_argument(
        "--asr-fallback",
        choices=("auto", "never", "force"),
        default="auto",
        help="Use whisper.cpp ASR when no subtitle exists; force regenerates ASR subtitles.",
    )
    cap.add_argument("--asr-model", default=DEFAULT_ASR_MODEL, choices=sorted(WHISPER_MODEL_URLS))
    cap.add_argument("--asr-model-path", help="Explicit whisper.cpp ggml model path.")
    cap.add_argument("--asr-download-model", action="store_true", help="Download the selected ASR model if missing.")
    cap.add_argument("--asr-threads", type=int, default=2)
    cap.add_argument("--asr-processors", type=int, default=6)
    cap.set_defaults(func=capture)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
