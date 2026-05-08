# Lab 05: Guardrails, Evals, Tracing

## 目标

从能跑变成能判断质量。

## 要学的东西

- Input guardrails
- Output guardrails
- Human-in-the-loop
- Tracing
- Eval dataset

## 最小实验

基于前面的客服 Agent：

- 阻止越权请求。
- 对退款、发邮件、改状态等动作加入人工批准。
- 准备 20 到 50 条测试样本。
- 记录失败案例和修复方式。

## 验收标准

- 有可重复运行的 eval 样本。
- 至少一个高风险动作需要人工批准。
- 每次失败都能从 trace 里定位原因。
- 不再只凭主观感觉判断 Agent 是否可用。

