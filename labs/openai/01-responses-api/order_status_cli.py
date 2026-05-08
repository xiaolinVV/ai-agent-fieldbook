from __future__ import annotations

import argparse
import json
import os
from typing import Any

from openai import OpenAI


DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")

SYSTEM_INSTRUCTIONS = """
You are a customer support assistant for a small demo store.
If the user asks about an order or gives an order id, call get_order_status before answering.
Return the final answer using the provided structured output schema.
""".strip()

ORDERS: dict[str, dict[str, str | None]] = {
    "ORDER-1001": {
        "status": "shipped",
        "eta": "2026-05-10",
        "last_update": "Package left the Shanghai sorting center.",
    },
    "ORDER-1002": {
        "status": "processing",
        "eta": "2026-05-12",
        "last_update": "Payment confirmed; waiting for warehouse pickup.",
    },
    "ORDER-1003": {
        "status": "delayed",
        "eta": None,
        "last_update": "Carrier reported a weather delay; new ETA is not confirmed.",
    },
}

GET_ORDER_STATUS_TOOL: dict[str, Any] = {
    "type": "function",
    "name": "get_order_status",
    "description": (
        "Look up a demo store order by order_id. Use this for questions about order "
        "status, shipping, delivery ETA, or missing orders. The order_id format is "
        "ORDER-1001."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "order_id": {
                "type": "string",
                "description": "Order id to look up, for example ORDER-1001.",
            }
        },
        "required": ["order_id"],
        "additionalProperties": False,
    },
    "strict": True,
}

FINAL_TEXT_FORMAT: dict[str, Any] = {
    "format": {
        "type": "json_schema",
        "name": "order_status_answer",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
                "found": {"type": "boolean"},
                "status": {"type": "string"},
                "eta": {"type": ["string", "null"]},
                "summary": {"type": "string"},
                "next_action": {"type": "string"},
            },
            "required": [
                "order_id",
                "found",
                "status",
                "eta",
                "summary",
                "next_action",
            ],
            "additionalProperties": False,
        },
    },
    "verbosity": "low",
}


def normalize_order_id(order_id: str) -> str:
    return order_id.strip().upper()


def get_order_status(order_id: str) -> dict[str, Any]:
    normalized = normalize_order_id(order_id)
    record = ORDERS.get(normalized)

    # Found and not-found orders intentionally share one shape.
    if record is None:
        return {
            "order_id": normalized,
            "found": False,
            "status": "not_found",
            "eta": None,
            "last_update": "No matching order exists in the demo database.",
        }

    return {
        "order_id": normalized,
        "found": True,
        "status": record["status"],
        "eta": record["eta"],
        "last_update": record["last_update"],
    }


def model_controls(model: str) -> dict[str, Any]:
    controls: dict[str, Any] = {}
    if model.startswith("gpt-5") or model.startswith("o"):
        controls["reasoning"] = {"effort": "low"}
    return controls


def output_item_types(response: Any) -> list[str]:
    return [getattr(item, "type", "unknown") for item in response.output]


def dump_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def call_named_tool(tool_call: Any) -> dict[str, Any]:
    if tool_call.name != "get_order_status":
        return {
            "error": f"Unsupported tool: {tool_call.name}",
            "supported_tools": ["get_order_status"],
        }

    arguments = json.loads(tool_call.arguments)
    return get_order_status(arguments["order_id"])


def run_order_lookup(order_id: str, model: str, show_raw: bool) -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set. Set it before running the API lab.")

    client = OpenAI()
    normalized_order_id = normalize_order_id(order_id)

    first_response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": SYSTEM_INSTRUCTIONS},
            {"role": "user", "content": f"请查询订单 {normalized_order_id} 的状态。"},
        ],
        tools=[GET_ORDER_STATUS_TOOL],
        tool_choice="auto",
        parallel_tool_calls=False,
        text={"verbosity": "low"},
        **model_controls(model),
    )

    function_outputs: list[dict[str, str]] = []
    tool_results: list[dict[str, Any]] = []

    for item in first_response.output:
        if getattr(item, "type", None) != "function_call":
            continue

        tool_result = call_named_tool(item)
        tool_results.append(tool_result)
        function_outputs.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps(tool_result, ensure_ascii=False),
            }
        )

    if not function_outputs:
        print(dump_json({
            "first_response_id": first_response.id,
            "first_response_output_item_types": output_item_types(first_response),
            "final_text": first_response.output_text,
        }))
        return

    final_response = client.responses.create(
        model=model,
        previous_response_id=first_response.id,
        input=function_outputs,
        text=FINAL_TEXT_FORMAT,
        **model_controls(model),
    )

    try:
        final_answer = json.loads(final_response.output_text)
    except json.JSONDecodeError:
        final_answer = {"raw_output_text": final_response.output_text}

    result = {
        "model": model,
        "first_response_id": first_response.id,
        "first_response_output_item_types": output_item_types(first_response),
        "tool_results": tool_results,
        "final_response_id": final_response.id,
        "final_response_output_item_types": output_item_types(final_response),
        "final_answer": final_answer,
    }

    if show_raw:
        result["raw_first_response_output"] = [
            item.model_dump() if hasattr(item, "model_dump") else str(item)
            for item in first_response.output
        ]
        result["raw_final_response_output"] = [
            item.model_dump() if hasattr(item, "model_dump") else str(item)
            for item in final_response.output
        ]

    print(dump_json(result))


def run_local_tool(order_id: str) -> None:
    print(dump_json(get_order_status(order_id)))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lab 01: Responses API function calling order-status demo.",
    )
    parser.add_argument(
        "order_id",
        nargs="?",
        default="ORDER-1001",
        help="Demo order id, for example ORDER-1001.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="OpenAI model id. Defaults to OPENAI_MODEL or gpt-5.5.",
    )
    parser.add_argument(
        "--show-raw",
        action="store_true",
        help="Include raw response output items for field inspection.",
    )
    parser.add_argument(
        "--local-tool-only",
        action="store_true",
        help="Run only the local demo tool; does not call the OpenAI API.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.local_tool_only:
        run_local_tool(args.order_id)
        return

    run_order_lookup(args.order_id, args.model, args.show_raw)


if __name__ == "__main__":
    main()
