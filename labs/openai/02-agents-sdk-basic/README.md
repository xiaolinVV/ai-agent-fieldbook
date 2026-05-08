# Lab 02: Agents SDK Basic

## 目标

用 OpenAI Agents SDK 做一个单 Agent。

## 要学的东西

- Agent 定义
- Runner / run
- function tool
- session
- tracing

## 最小实验

做一个客服 Agent：

- 工具 1：查询订单状态
- 工具 2：查询退款规则
- Agent 根据用户问题决定是否调用工具

## 验收标准

- Agent 能回答普通问题。
- Agent 能调用至少两个工具。
- 能在 trace 中看到模型调用和工具调用。
- instructions 不超过必要长度，业务逻辑不塞进长 prompt。

