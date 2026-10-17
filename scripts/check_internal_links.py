#!/usr/bin/env python3
"""Check local href/src targets in a built static site."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}

class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.targets.append(value.strip())

def resolve_target(site_root: Path, source_file: Path, raw_target: str) -> Path | None:
    parsed = urlsplit(raw_target)
    if parsed.scheme.lower() in IGNORED_SCHEMES or parsed.netloc or not parsed.path:
        return None
    path_text = unquote(parsed.path)
    target = (site_root / path_text.lstrip("/")) if path_text.startswith("/") else (source_file.parent / path_text)
    target = target.resolve()
    root = site_root.resolve()
    try:
        target.relative_to(root)
    except ValueError:
        return None
    candidates = [target]
    if target.is_dir() or parsed.path.endswith("/"):
        candidates.insert(0, target / "index.html")
    elif not target.suffix:
        candidates.extend([target.with_suffix(".html"), target / "index.html"])
    return next((candidate for candidate in candidates if candidate.is_file()), target)

def main() -> int:
    site_root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    if not site_root.is_dir():
        print(f"ERROR: built site directory not found: {site_root}", file=sys.stderr)
        return 2
    html_files = sorted(site_root.rglob("*.html"))
    if not html_files:
        print(f"ERROR: no HTML files found under {site_root}", file=sys.stderr)
        return 2
    failures: list[str] = []
    for source in html_files:
        parser = LinkCollector()
        parser.feed(source.read_text(encoding="utf-8"))
        for raw_target in parser.targets:
            resolved = resolve_target(site_root, source, raw_target)
            if resolved is not None and not resolved.is_file():
                failures.append(f"{source.relative_to(site_root)} -> {raw_target}")
    if failures:
        print("Broken local links:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print(f"Checked local href/src targets in {len(html_files)} HTML files; no broken local targets found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
