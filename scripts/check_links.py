#!/usr/bin/env python3
"""Fail if any Markdown file links to a relative path that does not exist."""
import pathlib
import re
import sys
from urllib.parse import unquote

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
root = pathlib.Path(__file__).resolve().parent.parent
broken = []
for md in sorted(root.rglob("*.md")):
    if any(p.startswith(".") or p == "node_modules" for p in md.relative_to(root).parts[:-1]):
        continue
    text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
    for target in LINK.findall(text):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        path = unquote(target.split("#", 1)[0])
        if not path:
            continue
        resolved = (root / path.lstrip("/")) if path.startswith("/") else (md.parent / path)
        if not resolved.exists():
            broken.append(f"{md.relative_to(root)}: {target}")
if broken:
    print("Broken relative links:\n  " + "\n  ".join(broken))
    sys.exit(1)
print("All relative Markdown links resolve.")
