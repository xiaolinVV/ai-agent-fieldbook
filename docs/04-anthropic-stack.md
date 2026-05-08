# Anthropic / Claude Agent 技术栈

这一阶段放在 OpenAI 官方栈之后。原因很简单：先学透一套官方体系，再做横向比较。否则只是把两个生态的概念搅成一团。

## 学习目标

- 掌握 Claude Messages API 的基本调用模型。
- 掌握 Claude tool use。
- 理解 MCP 在工具连接中的角色。
- 学习 Claude Agent SDK。
- 学习 computer use 的适用边界。
- 对比 OpenAI Agents SDK 与 Claude Agent SDK 的工程取舍。

## 建议顺序

### 2.1 Claude Messages API

目标：

- 理解 Claude 的消息输入输出。
- 理解 system prompt、user message、assistant message 的结构。
- 跑通最小调用。

交付物：

- 一个最小 Claude CLI。

### 2.2 Tool Use

目标：

- 定义工具 schema。
- 让 Claude 请求工具调用。
- 把工具结果返回给 Claude。

交付物：

- 一个订单查询工具实验。

### 2.3 Model Context Protocol

目标：

- 理解 MCP client/server 模型。
- 写一个最小 MCP server。
- 让 Agent 调用 MCP 工具。

交付物：

- 一个本地资料查询 MCP server。

### 2.4 Claude Agent SDK

目标：

- 理解 Claude Agent SDK 的 Agent 定义和运行方式。
- 与 OpenAI Agents SDK 对比。

交付物：

- 一个 Claude 版客服 Agent。

### 2.5 Computer Use

目标：

- 理解 computer use 的能力边界和风险。
- 明确什么时候应该用 API，什么时候才用 UI 自动化。

交付物：

- 一个低风险浏览器自动化实验。

## 对比维度

Phase 2 结束时写一份对比文档：

- Agent 定义方式
- 工具调用方式
- 状态管理
- 多 Agent 编排
- MCP 支持
- sandbox / computer use
- tracing / observability
- evals
- 部署复杂度
- 适合的产品场景

