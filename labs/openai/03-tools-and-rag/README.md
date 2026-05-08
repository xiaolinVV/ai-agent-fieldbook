# Lab 03: Tools and Retrieval

## 目标

让 Agent 接入真实信息源，并明确区分模型记忆、web search 和 file search。

## 要学的东西

- Function tools
- Web search
- File search
- Remote MCP
- Code interpreter

本实验先做最小切面：

- `web_search`: 查公开网页。
- `file_search`: 查本地资料上传后的 vector store。

Remote MCP 和 Code interpreter 不在本次最小实验里，后面单独拆。一次塞太多工具，只会把问题搅浑。

官方资料：

- https://developers.openai.com/api/docs/guides/tools-web-search
- https://developers.openai.com/api/docs/guides/tools-file-search
- https://developers.openai.com/api/docs/guides/tools
- https://platform.openai.com/docs/api-reference/vector-stores
- https://platform.openai.com/docs/api-reference/files/create

## 最小实验

做一个资料研究助手：

- 用户输入研究主题。
- Agent 使用 web search 找公开资料。
- Agent 使用 file search 查本地资料。
- 输出摘要、引用和下一步建议。

实现文件：

- `research_assistant_cli.py`

本地资料：

- `data/openai-agent-local-notes.md`

核心数据流：

```text
本地 markdown 资料
  ↓
client.files.create(purpose="assistants")
  ↓
client.vector_stores.create(file_ids=[...])
  ↓
client.responses.create(
    tools=[
      {"type": "web_search"},
      {"type": "file_search", "vector_store_ids": [...]}
    ]
  )
  ↓
response.output 里观察 web_search_call / file_search_call
  ↓
输出 final_answer、URL citation、file_search results
```

## 依赖

本仓库使用 `uv`：

```bash
uv sync
```

需要设置 OpenAI API key：

```bash
export OPENAI_API_KEY="你的 key"
```

默认模型使用 `gpt-5.5`，也可以覆盖：

```bash
export OPENAI_MODEL="gpt-5.5"
```

## 运行

先验证本地资料搜索，不调用 API：

```bash
uv run python labs/openai/03-tools-and-rag/research_assistant_cli.py \
  "工具边界" \
  --local-search-only
```

创建 vector store：

```bash
uv run python labs/openai/03-tools-and-rag/research_assistant_cli.py \
  --prepare-vector-store
```

命令会输出 `vector_store_id`。拿到它后运行完整实验：

```bash
uv run python labs/openai/03-tools-and-rag/research_assistant_cli.py \
  "OpenAI Agent 工具边界和检索能力应该怎么设计？" \
  --vector-store-id "vs_xxx"
```

如果要上传额外本地资料：

```bash
uv run python labs/openai/03-tools-and-rag/research_assistant_cli.py \
  --prepare-vector-store \
  --file docs/03-openai-stack.md \
  --file notes/2026-05-08-openai-responses-api-lab01.md
```

## 输出说明

完整实验输出是 JSON，重点看：

- `output_item_types`: 是否出现 `web_search_call` 和 `file_search_call`。
- `file_search_results`: file search 返回的本地资料片段。
- `url_citations`: web search 产生的 URL 引用。
- `final_answer`: 模型结合两类来源后的最终回答。

## 验收标准

- 至少使用两类工具。
- 输出中标明资料来源。
- 工具失败时有明确错误信息。
- 不把检索结果伪装成模型记忆。

## 工程判断

值得做：

- 资料问答需要同时覆盖公开网页和内部资料。
- 需要把来源交给用户审查。
- 需要区分“模型知道的”和“刚检索到的”。

不值得做：

- 只查一个固定本地表格，却引入完整 RAG。
- 文档很少，直接结构化进工具返回值更简单。
- 没有权限边界，却让模型随便查内部资料。

工具越多越危险。先让两个只读检索工具工作清楚，再谈 MCP 和代码执行。
