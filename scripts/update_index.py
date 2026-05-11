#!/usr/bin/env python3
"""Regenerate README skills table and marketplace.json from skills/*/SKILL.md frontmatter.

Run from repo root:
    python scripts/update_index.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

TABLE_START = "<!-- SKILLS-TABLE:START -->"
TABLE_END = "<!-- SKILLS-TABLE:END -->"


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        raise ValueError(f"{skill_md}: no YAML frontmatter")
    body = m.group(1)
    out: dict[str, str] = {}
    key = None
    buf: list[str] = []
    for line in body.splitlines():
        if re.match(r"^[A-Za-z_][\w-]*\s*:", line):
            if key is not None:
                out[key] = " ".join(s.strip() for s in buf).strip()
            key, _, rest = line.partition(":")
            key = key.strip()
            rest = rest.strip()
            buf = []
            if rest and rest != ">-" and rest != ">":
                buf.append(rest)
        else:
            buf.append(line.strip())
    if key is not None:
        out[key] = " ".join(s.strip() for s in buf).strip()
    return out


def collect_skills() -> list[dict[str, str]]:
    skills = []
    for d in sorted(SKILLS_DIR.iterdir()):
        skill_md = d / "SKILL.md"
        if not skill_md.is_file():
            continue
        fm = parse_frontmatter(skill_md)
        name = fm.get("name") or d.name
        desc = fm.get("description", "").strip()
        # First sentence keeps the README table compact.
        short = re.split(r"(?<=[.。])\s+", desc, maxsplit=1)[0]
        skills.append({"dir": d.name, "name": name, "description": desc, "short": short})
    return skills


def render_table(skills: list[dict[str, str]]) -> str:
    lines = ["| Skill | Description |", "| ----- | ----------- |"]
    for s in skills:
        lines.append(f"| [{s['name']}](./skills/{s['dir']}) | {s['short']} |")
    return "\n".join(lines)


def update_readme(skills: list[dict[str, str]]) -> bool:
    text = README.read_text(encoding="utf-8")
    table = render_table(skills)
    block = f"{TABLE_START}\n{table}\n{TABLE_END}"
    if TABLE_START in text and TABLE_END in text:
        new = re.sub(
            re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END),
            block,
            text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        # Insert after the "## Available Skills" heading, replacing any existing
        # static table until the next "## " heading.
        pattern = r"(## Available Skills\n\n)(.*?)(\n## )"
        new = re.sub(pattern, lambda m: m.group(1) + block + "\n" + m.group(3), text, count=1, flags=re.DOTALL)
        if new == text:
            raise SystemExit("README.md: could not find '## Available Skills' section to update")
    if new != text:
        README.write_text(new, encoding="utf-8")
        return True
    return False


def update_marketplace(skills: list[dict[str, str]]) -> bool:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    skill_paths = [f"./skills/{s['dir']}" for s in skills]
    data["plugins"] = [
        {
            "name": "agent-skills",
            "description": "Personal collection of reusable agent skills",
            "source": "./",
            "strict": False,
            "skills": skill_paths,
        }
    ]
    new_text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    old_text = MARKETPLACE.read_text(encoding="utf-8")
    if new_text != old_text:
        MARKETPLACE.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    skills = collect_skills()
    if not skills:
        print("No skills found under skills/", file=sys.stderr)
        return 1
    changed_readme = update_readme(skills)
    changed_marketplace = update_marketplace(skills)
    print(f"Indexed {len(skills)} skill(s): {', '.join(s['name'] for s in skills)}")
    print(f"  README.md: {'updated' if changed_readme else 'no change'}")
    print(f"  marketplace.json: {'updated' if changed_marketplace else 'no change'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
