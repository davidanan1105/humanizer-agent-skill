---
name: humanizer-skill-zh
description: |
  将中文文本中的 AI 痕迹改写为更自然的人类表达。聚焦识别常见 AI 模式并进行简化、具体化与去模板化改写。
metadata:
  trigger: 编辑/审阅文本，去除 AI 写作痕迹
allowed-tools:
  - Read
  - Write
  - Edit
---

# Humanizer Skill（Agent-first）

## Quick Start（≤3 步）
1. 读取待处理文本。
2. 只在需要时读取 `references/` 里的细节规则。
3. 输出结构化结果（见下方格式）。

## 核心流程（≤6 条）
1. 诊断：识别 AI 模式与高频词（参考 `references/patterns.md`）。
2. 缩减：删掉填充短语与过度限定。
3. 具体化：用事实/细节替换抽象大词。
4. 去模板化：打破“三段式、否定式排比、官方口吻”。
5. 变节奏：混合长短句，避免机械等长句。
6. 复核：保留原意与语气，避免过度改写。

## 输出格式（结构化）
- `final_text`: 改写后的文本
- `changes_summary`: 改写说明（简短列表或一句话）
- `matched_patterns`（可选）: 命中的模式列表

> 规则细节按需参考：`references/`（patterns/principles/lexicon/examples）。
