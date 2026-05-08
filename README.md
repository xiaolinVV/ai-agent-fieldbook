# AI Agent Learning Lab

这个仓库用于系统学习 AI Agent 开发。第一阶段从 OpenAI 官方 Agent 技术栈开始，第二阶段学习 Anthropic/Claude 生态，第三阶段调研真实应用场景和开源项目。

核心原则很简单：

- 先学官方原语，再学框架包装。
- 先做单 Agent，再做多 Agent。
- 先把工具调用、状态、追踪、评估弄清楚，再谈复杂 orchestration。
- 学完必须拆真实项目，否则只是背文档。

## 仓库结构

```text
.
├── docs/
│   ├── 00-learning-principles.md
│   ├── 01-roadmap.md
│   ├── 02-official-resources.md
│   ├── 03-openai-stack.md
│   ├── 04-anthropic-stack.md
│   └── 05-field-research-plan.md
├── labs/
│   ├── openai/
│   │   ├── 01-responses-api/
│   │   ├── 02-agents-sdk-basic/
│   │   ├── 03-tools-and-rag/
│   │   ├── 04-orchestration-handoffs/
│   │   ├── 05-guardrails-evals-tracing/
│   │   └── 06-sandbox-agents/
│   └── anthropic/
├── research/
│   ├── open-source-projects/
│   └── use-cases/
└── notes/
```

## 学习阶段

### Phase 1: OpenAI 官方 Agent 技术栈

目标：掌握 OpenAI 官方 Agent 开发主线。

学习顺序：

1. Building agents 概念模型
2. Responses API
3. Agents SDK
4. Tools: function calling, web search, file search, MCP, code interpreter
5. Orchestration: handoffs, agent-as-tool, routing
6. Guardrails, tracing, evals
7. Sandbox agents 和长任务
8. 小型端到端项目

### Phase 2: Anthropic / Claude Agent 技术栈

目标：理解 Claude 生态的 Agent 开发方式，并和 OpenAI 栈对比。

学习顺序：

1. Claude Messages API
2. Tool use
3. Model Context Protocol
4. Claude Agent SDK
5. Computer use
6. Claude Code SDK
7. 与 OpenAI Agents SDK 做能力和工程边界对比

### Phase 3: 真实场景和开源项目拆解

目标：把官方知识落到真实系统里。

学习顺序：

1. 调研市面真实 Agent 应用场景
2. 筛选开源 Agent 项目
3. 拆解架构、工具边界、状态管理、评估方式
4. 复刻一个最小可用版本
5. 总结什么值得学，什么只是炫技

## 每个模块的交付物

每学一个模块，至少留下这几样东西：

- 一份学习笔记，放在 `notes/`
- 一个可运行实验，放在对应 `labs/` 子目录
- 一份问题清单：哪些地方官方文档没讲清楚
- 一份工程判断：这个能力适合什么场景，不适合什么场景

## 快速开始

准备环境变量：

```bash
cp .env.example .env
```

Python 路线建议使用 `uv` 或普通虚拟环境。第一阶段先不急着安装所有依赖，进入每个 lab 时按该 lab 的 README 安装需要的包。

## 当前状态

- [x] 初始化学习项目
- [x] 建立 OpenAI 第一阶段路线
- [x] 预留 Anthropic 第二阶段
- [x] 预留真实场景和开源项目调研阶段
- [x] 完成 Lab 01: Responses API 最小实验（完整 API 路径仍需 `OPENAI_API_KEY` 验证）
- [x] 开始 Lab 02: Agents SDK Basic
- [x] 开始 Lab 03: Tools and Retrieval
