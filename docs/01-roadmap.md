# 学习路线

这是一条循序渐进路线。默认节奏是 10 到 12 周，可以按实际时间压缩或拉长。

## Phase 1: OpenAI 官方 Agent 技术栈

### 1.1 Agent 基础模型

时间：0.5 到 1 天

资料：

- OpenAI Building agents track
- OpenAI Agents SDK overview
- OpenAI tools guide

目标：

- 明确 Agent 与普通聊天机器人的区别。
- 理解 instructions、tools、state、orchestration、guardrails、evals 的关系。
- 画出 OpenAI Agent 技术栈图。

交付物：

- `notes/openai-agent-mental-model.md`
- 一张 Mermaid 架构图

### 1.2 Responses API

时间：1 到 2 天

目标：

- 掌握 Responses API 的输入、输出、状态和工具调用模型。
- 跑通最小文本响应。
- 加入 function tool。
- 加入 structured output。
- 理解为什么新项目不应该默认从旧 Chat Completions 设计开始。

实验目录：

- `labs/openai/01-responses-api/`

交付物：

- 一个 CLI 小程序：输入订单号，调用本地工具查询模拟订单状态，输出结构化结果。

### 1.3 Agents SDK 基础

时间：1 到 2 天

目标：

- 创建单 Agent。
- 通过 SDK 运行 Agent。
- 添加 function tool。
- 观察 trace。
- 理解 SDK 比 Responses API 多做了什么。

实验目录：

- `labs/openai/02-agents-sdk-basic/`

交付物：

- 一个单 Agent 客服助手。
- 至少两个工具：查询订单、查询退款规则。

### 1.4 Tools 与检索能力

时间：2 到 3 天

目标：

- Function calling
- Web search
- File search
- Remote MCP
- Code interpreter

实验目录：

- `labs/openai/03-tools-and-rag/`

交付物：

- 一个资料研究助手：能结合 web search 和本地资料回答问题，并给出引用。

### 1.5 Orchestration 与 Handoffs

时间：2 到 3 天

目标：

- 理解 handoff 与 agent-as-tool 的差异。
- 创建 triage agent。
- 创建多个 specialist agents。
- 明确每个 Agent 的工具边界。

实验目录：

- `labs/openai/04-orchestration-handoffs/`

交付物：

- 一个多 Agent 客服流转系统：账务、技术支持、资料研究三个方向。

### 1.6 Guardrails、Tracing、Evals

时间：2 到 4 天

目标：

- 输入 guardrail
- 输出 guardrail
- Human-in-the-loop
- Trace 分析
- Eval dataset

实验目录：

- `labs/openai/05-guardrails-evals-tracing/`

交付物：

- 20 到 50 条测试样本。
- 一份 trace 复盘。
- 一个需要人工批准的高风险工具调用。

### 1.7 Sandbox Agents

时间：3 到 5 天

目标：

- 理解 sandbox agent 的边界。
- 让 Agent 在受控目录里读文件、写报告、运行命令。
- 学会限制权限和审查输出。

实验目录：

- `labs/openai/06-sandbox-agents/`

交付物：

- 一个文档分析 Agent：读取 `data/`，生成 `report.md`。

### 1.8 OpenAI 阶段项目

时间：3 到 7 天

目标：

- 把 Responses API、Agents SDK、tools、handoffs、guardrails、tracing、evals 组合成一个小系统。

推荐项目：

- 企业资料研究与工单处理 Agent

最小功能：

- 用户提出问题。
- Agent 查询内部资料和外部网页。
- 必要时创建工单 JSON。
- 高风险动作需要人工批准。
- 每次运行可追踪。
- 有最小 eval 集合。

## Phase 2: Anthropic / Claude Agent 技术栈

时间：2 到 4 周

目标：

- 学习 Claude tool use。
- 学习 Model Context Protocol。
- 学习 Claude Agent SDK。
- 学习 computer use。
- 对比 OpenAI 和 Anthropic 的 Agent 开发边界。

交付物：

- `docs/anthropic-vs-openai-agent-stack.md`
- 一个 Claude 版本的最小客服 Agent。
- 一个 MCP server 小实验。

## Phase 3: 真实应用场景和开源项目拆解

时间：2 到 4 周

目标：

- 调研真实应用场景。
- 拆解开源项目。
- 复刻一个最小版本。
- 总结可复用模式。

研究方向：

- 客服与售后
- 企业知识库
- 代码 Agent
- 浏览器自动化
- 数据分析 Agent
- 销售/运营工作流
- 文档处理和投研

交付物：

- `research/use-cases/*.md`
- `research/open-source-projects/*.md`
- 一个复刻项目

