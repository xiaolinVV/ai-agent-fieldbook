# Lab 01: Responses API

## 目标

理解 OpenAI Agent 技术栈的底层原语。

## 要学的东西

- Responses API 基本调用
- 输入与输出结构
- function tool
- structured output
- conversation state
- streaming

## 最小实验

做一个 CLI：

```text
用户输入订单号
  ↓
模型判断是否需要查订单
  ↓
调用本地 get_order_status(order_id)
  ↓
输出结构化结果
```

## 验收标准

- 能运行最小 Responses API 调用。
- 能看到一次工具调用。
- 输出是结构化 JSON。
- 能解释 response 中哪些字段表示模型输出，哪些字段表示工具调用。

