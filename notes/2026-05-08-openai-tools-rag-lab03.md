# OpenAI Tools and Retrieval Lab 03

日期：2026-05-08

## 今天读了什么

- OpenAI web search tool guide
- OpenAI file search tool guide
- OpenAI built-in tools guide
- OpenAI vector stores API reference
- OpenAI files API reference

官方资料：

- https://developers.openai.com/api/docs/guides/tools-web-search
- https://developers.openai.com/api/docs/guides/tools-file-search
- https://developers.openai.com/api/docs/guides/tools
- https://platform.openai.com/docs/api-reference/vector-stores
- https://platform.openai.com/docs/api-reference/files/create

## 跑了什么实验

新增实验文件：

- `labs/openai/03-tools-and-rag/research_assistant_cli.py`
- `labs/openai/03-tools-and-rag/data/openai-agent-local-notes.md`

实验目标：

```text
用户输入研究主题
  -> web_search 查询公开资料
  -> file_search 查询本地 vector store
  -> 输出摘要、URL citation、file search results
```

本地资料搜索验证命令：

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

完整 API 验证命令：

```bash
uv run python labs/openai/03-tools-and-rag/research_assistant_cli.py \
  "OpenAI Agent 工具边界和检索能力应该怎么设计？" \
  --vector-store-id "vs_xxx"
```

## 关键理解

Lab 03 的核心不是“做一个高级 RAG”，而是把信息来源分清楚。

模型自己的参数记忆、web search、file search 是三件事：

- 模型记忆：不适合回答最新事实，也不能当引用来源。
- web search：适合公开、变化的信息，会产生 URL 来源。
- file search：适合项目资料、学习笔记、产品文档这类本地或私有资料。

Vector store 是 file search 的前置条件。本地文件不是直接塞给模型，而是先：

```text
client.files.create(...)
  -> client.vector_stores.create(file_ids=[...])
  -> responses.create(tools=[{"type": "file_search", "vector_store_ids": [...]}])
```

工具调用输出也要观察，而不是只看最终回答。Lab 03 输出里保留：

- `output_item_types`
- `file_search_results`
- `url_citations`
- `final_answer`

## 工程判断

这个能力适合：

- 企业知识库 + 公开资料对照。
- 学习笔记检索。
- 产品文档、政策文档、FAQ 的引用式问答。

这个能力不适合：

- 资料只有几条固定规则。那直接写 function tool 更清楚。
- 高风险内部资料没有权限控制。检索也是权限边界，不是免费通行证。
- 为了“看起来像 RAG”把所有内容都扔进 vector store。数据结构错了，再多检索也是垃圾。

## 不清楚的问题

- 当前环境没有设置 `OPENAI_API_KEY`，所以 `web_search` 和 `file_search` 的真实 API 路径还没验证。
- 需要观察一次真实响应后，确认 `output_item_types` 里 web/file search call 的具体顺序。
- 需要比较：Responses API 内置 file search 与手写本地检索工具，在哪些场景下哪个更简单。
