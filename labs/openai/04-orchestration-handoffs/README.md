# Lab 04: Orchestration and Handoffs

## 目标

理解什么时候需要多个 Agent。

## 要学的东西

- Handoff
- Agent as tool
- Routing agent
- Specialist agents
- 工具边界

## 最小实验

做一个多 Agent 客服系统：

- `TriageAgent`: 判断问题类型
- `BillingAgent`: 账务问题
- `TechSupportAgent`: 技术支持
- `ResearchAgent`: 资料研究

## 验收标准

- 能解释为什么需要拆成多个 Agent。
- 每个 Agent 的工具不同。
- trace 中能看到 handoff 或 agent-as-tool。
- 删除任意一个 specialist 时，系统行为边界清楚。

