#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path


def load_patterns(patterns_path: Path):
    patterns = []
    current = None
    in_keywords = False

    for raw_line in patterns_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line.startswith("- id:"):
            if current:
                patterns.append(current)
            current = {"id": line.split(":", 1)[1].strip(), "name": "", "keywords": []}
            in_keywords = False
            continue
        if current is None:
            continue
        if line.startswith("  name:"):
            current["name"] = line.split(":", 1)[1].strip()
            continue
        if line.startswith("  keywords:"):
            in_keywords = True
            continue
        if in_keywords:
            match = re.match(r"\s*-\s*(.+)", line)
            if match:
                current["keywords"].append(match.group(1).strip())
            else:
                in_keywords = False

    if current:
        patterns.append(current)
    return patterns


def read_input(input_path: str | None):
    if input_path:
        return Path(input_path).read_text(encoding="utf-8")
    data = sys.stdin.read()
    if not data:
        raise SystemExit("No input provided. Use --input or stdin.")
    return data


def diagnose_text(text: str, patterns):
    matches = []
    for pattern in patterns:
        hits = [kw for kw in pattern.get("keywords", []) if kw and kw in text]
        if hits:
            matches.append({
                "id": pattern.get("id"),
                "name": pattern.get("name"),
                "hits": hits,
            })
    return matches


def main():
    parser = argparse.ArgumentParser(description="Diagnose AI writing patterns from text.")
    parser.add_argument("--input", "-i", help="Input file path. Reads stdin if omitted.")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parents[1]
    patterns_path = base_dir / "references" / "patterns.md"
    patterns = load_patterns(patterns_path)
    text = read_input(args.input)
    matched = diagnose_text(text, patterns)

    output = {
        "matched_patterns": matched,
        "total_matches": len(matched),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
