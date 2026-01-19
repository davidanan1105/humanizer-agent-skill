#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

import diagnose


REPLACEMENTS = [
    ("此外，", ""),
    ("此外", ""),
    ("然而，", ""),
    ("然而", ""),
    ("值得注意的是", ""),
    ("在这个时间点", "现在"),
    ("可以潜在地可能", "可能"),
    ("不仅仅是", ""),
    ("这不仅仅是", "这"),
    ("而是", ""),
    ("希望这对您有帮助", ""),
    ("请告诉我", ""),
]


def read_input(input_path: str | None):
    if input_path:
        return Path(input_path).read_text(encoding="utf-8")
    data = sys.stdin.read()
    if not data:
        raise SystemExit("No input provided. Use --input or stdin.")
    return data


def apply_replacements(text: str):
    changes = []
    for old, new in REPLACEMENTS:
        if old in text:
            text = text.replace(old, new)
            changes.append(f"replace '{old}' -> '{new}'")
    if "—" in text:
        text = text.replace("—", "，")
        changes.append("replace '—' -> '，'")

    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"[，,]{2,}", "，", text)
    text = text.strip()
    return text, changes


def humanize_text(text: str):
    base_dir = Path(__file__).resolve().parents[1]
    patterns_path = base_dir / "references" / "patterns.md"
    patterns = diagnose.load_patterns(patterns_path)
    matched = diagnose.diagnose_text(text, patterns)

    rewritten, changes = apply_replacements(text)
    if not changes:
        changes_summary = ["no deterministic replacements applied; consider manual rewrite"]
    else:
        changes_summary = changes

    return {
        "final_text": rewritten,
        "changes_summary": changes_summary,
        "matched_patterns": matched,
    }


def main():
    parser = argparse.ArgumentParser(description="Humanize text with simple heuristics.")
    parser.add_argument("--input", "-i", help="Input file path. Reads stdin if omitted.")
    args = parser.parse_args()

    text = read_input(args.input)
    result = humanize_text(text)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
