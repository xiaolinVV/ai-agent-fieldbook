# OpenAI Agent Local Notes

## 工具边界

工具是 Agent 和外部世界之间的边界。读工具和写工具应该分开。查询订单、
读取资料、搜索文档是低风险读操作；退款、发邮件、改数据库、执行 shell 是高风险
写操作，默认需要人工批准。

## Responses API 与 Agents SDK

Responses API 是底层原语，直接暴露输入、输出、工具调用和状态链路。Lab 01 使用
Responses API 手写 function tool loop，重点是理解 `function_call`、`call_id` 和
`function_call_output`。

Agents SDK 是上层框架。Lab 02 使用 `Agent`、`Runner`、function tool、session 和
trace，重点是观察 SDK 如何替应用代码管理工具循环。

## 检索能力

Web search 适合查公开、可能变化的信息。File search 适合查私有文档、学习笔记、
产品手册和项目资料。两者都不是模型记忆，回答时应该说明资料来源。

## 工程判断

不要为了显得高级把所有工具一次性暴露给模型。工具越多，选择错误和权限错误的风险
越高。先做少量只读工具，把输入输出结构、失败路径和引用来源跑清楚，再考虑复杂编排。
