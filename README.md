**For agents:** start from `SKILL.md`  
**For humans:** start from `README.md`


# humanizer-skill-zh

一句话用途：用“Agent-first/渐进式披露”结构，把 AI 味文本改成更像人写的中文。  

**30 秒上手**
1. 复制 SKILL.md 到你的 Agent/Skill 系统中。  
2. 需要规则时再按需读取 `references/`。  
3. 本地 CLI：`python scripts/humanize.py < input.txt`。  

## 作为 Skill 使用
- 入口说明见：`SKILL.md`。  
- 规则细节按需加载：`references/`（避免一次性占用 token）。  

## 可选 CLI 用法（最小可运行）
```bash
python scripts/humanize.py < input.txt
python scripts/humanize.py --input input.txt
```

> 说明：`scripts/humanize.py` 会先调用 `diagnose.py` 做匹配，再执行规则启发式改写，输出结构化结果。
