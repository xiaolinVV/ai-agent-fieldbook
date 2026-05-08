# OpenAI Agent 技术栈

## 技术栈分层

```text
用户请求
  ↓
应用层：CLI / Web App / Workflow
  ↓
Agent 编排层：Agents SDK / Agent Builder
  ↓
模型与状态层：Responses API
  ↓
工具层：function tools / web search / file search / MCP / code interpreter / sandbox
  ↓
外部系统：数据库 / 文件 / 第三方 API / 浏览器 / shell
```

## 该先学什么

### Responses API

Responses API 是底层原语。它负责模型响应、状态、多模态输入和工具调用。

必须掌握：

- 输入消息结构
- 输出 item
- tool call
- structured output
- previous response / conversation state
- streaming

### Agents SDK

Agents SDK 是上层框架。它把 Agent 定义、工具、handoff、guardrail、trace 等能力组织起来。

必须掌握：

- `Agent`
- `Runner` / run loop
- function tools
- handoffs
- sessions
- tracing
- guardrails
- evals

### Tools

工具是 Agent 做事的边界。工具定义不好，Agent 系统一定烂。

学习顺序：

1. Function tool
2. Web search
3. File search
4. Code interpreter
5. Remote MCP
6. Sandbox filesystem / shell
7. Computer use

### Agent Builder 与 ChatKit

这是产品化路线，不是替代 SDK 的万能方案。

适合：

- 快速原型
- 聊天 UI 嵌入
- 业务人员参与配置 workflow

不适合：

- 强业务权限
- 深度后端集成
- 复杂状态控制
- 严格审计逻辑

## OpenAI 第一阶段实验清单

| 阶段 | 实验 | 核心问题 |
| --- | --- | --- |
| 01 | Responses API CLI | 底层输入输出和工具调用是什么 |
| 02 | Single Agent | SDK 如何组织 Agent 和 tool |
| 03 | Research Agent | web/file search 如何进入工作流 |
| 04 | Multi-Agent Support | handoff 什么时候有价值 |
| 05 | Guardrails/Evals | 如何判断系统是否可靠 |
| 06 | Sandbox Agent | Agent 如何安全处理文件和命令 |

## OpenAI 阶段完成标准

完成 Phase 1 时必须能回答：

- Responses API 和 Agents SDK 的边界是什么？
- function tool 和 built-in tool 的差异是什么？
- handoff 和 agent-as-tool 什么时候用？
- guardrails 应该挡什么？
- trace 如何帮助定位问题？
- eval dataset 应该怎么设计？
- sandbox agent 的权限边界在哪里？

