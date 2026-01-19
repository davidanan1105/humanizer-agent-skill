# Patterns（AI 痕迹模式）

> 说明：本文件包含可机器读取的模式索引，`scripts/diagnose.py` 会用关键词进行简单匹配。

## Pattern Index（machine-readable）
- id: exaggeration
  name: 过度强调意义/遗产/趋势
  keywords:
    - 标志着
    - 象征
    - 关键时刻
    - 持久的
- id: fame
  name: 过度强调知名度与媒体报道
  keywords:
    - 媒体
    - 引用
    - 报道
    - 粉丝
- id: ing_phrase
  name: 以“-ing/现在分词式”结尾的肤浅分析
  keywords:
    - 反映
    - 彰显
    - 确保
    - 展示
- id: promo
  name: 宣传/广告式语言
  keywords:
    - 令人叹为观止
    - 迷人的
    - 开创性的
    - 充满活力的
- id: vague_attribution
  name: 模糊归因与含糊措辞
  keywords:
    - 专家认为
    - 观察者指出
    - 行业报告显示
    - 多个来源
- id: challenge_outlook
  name: 提纲式“挑战与展望”
  keywords:
    - 尽管存在这些挑战
    - 未来展望
    - 面临若干挑战
- id: ai_lexicon
  name: 过度使用 AI 词汇
  keywords:
    - 此外
    - 至关重要
    - 深入探讨
    - 复杂性
- id: copula_avoidance
  name: 回避“是”
  keywords:
    - 作为
    - 充当
    - 设有
    - 提供
- id: neg_parallel
  name: 否定式排比
  keywords:
    - 不仅仅是
    - 而是
- id: rule_of_three
  name: 三段式法则
  keywords:
    - 三个方面
    - 包括
    - 以及
- id: synonym_spin
  name: 刻意换词（同义词循环）
  keywords:
    - 主人公
    - 主要角色
    - 中心人物
- id: false_range
  name: 虚假范围
  keywords:
    - 从
    - 到
- id: em_dash
  name: 破折号过度使用
  keywords:
    - —
- id: bold_overuse
  name: 粗体过度使用
  keywords:
    - **
- id: inline_headings
  name: 内联标题垂直列表
  keywords:
    - **用户体验：**
    - **性能：**
- id: title_case
  name: 标题大小写（中文多为不适用）
  keywords:
    - ##
- id: emoji
  name: 表情符号装饰
  keywords:
    - 🚀
    - ✅
    - 💡
- id: curly_quotes
  name: 弯引号/英文引号混用
  keywords:
    - “
    - ”
- id: chatty
  name: 协作式对话痕迹
  keywords:
    - 希望这对您有帮助
    - 请告诉我
    - 当然
- id: knowledge_cutoff
  name: 知识截止日期免责声明
  keywords:
    - 截至
    - 训练更新
    - 基于可用信息
- id: flattery
  name: 谄媚/卑躬屈膝
  keywords:
    - 您说得完全正确
    - 好问题
- id: filler
  name: 填充短语
  keywords:
    - 在这个时间点
    - 值得注意的是
    - 为了实现这一目标
- id: hedging
  name: 过度限定
  keywords:
    - 可能会
    - 可以潜在地
    - 某种程度上
- id: generic_positive
  name: 通用积极结论
  keywords:
    - 未来看起来光明
    - 激动人心的时代

## 说明（人读版）
- 模式名称与问题描述来自原始 SKILL 规则。
- 机器检测仅做粗匹配，不代表最终判断。
