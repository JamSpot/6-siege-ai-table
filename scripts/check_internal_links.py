#!/usr/bin/env python3
"""Check built-site local links, assets, and HTML fragment targets."""
from __future__ import annotations
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}

class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[tuple[str, str]] = []
        self.anchors: set[str] = set()
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for key in ("id", "name"):
            if values.get(key):
                self.anchors.add(values[key])
        for key in ("href", "src"):
            if values.get(key):
                self.targets.append((key, values[key].strip()))

def read_baseurl() -> str:
    config = Path("_config.yml")
    if not config.is_file():
        return ""
    for line in config.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("baseurl:"):
            return line.split(":", 1)[1].strip().strip("\\"'").rstrip("/")
    return ""

def resolve_target(root: Path, source: Path, raw: str, baseurl: str) -> tuple[Path | None, str]:
    parsed = urlsplit(raw)
    if parsed.scheme.lower() in IGNORED_SCHEMES or parsed.netloc:
        return None, ""
    path = unquote(parsed.path)
    if baseurl and (path == baseurl or path.startswith(baseurl + "/")):
        path = path[len(baseurl):] or "/"
    target = source if not path else (root / path.lstrip("/") if path.startswith("/") else source.parent / path)
    target = target.resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return None, ""
    candidates = [target]
    if target.is_dir() or parsed.path.endswith("/"):
        candidates.insert(0, target / "index.html")
    elif not target.suffix:
        candidates.extend((target.with_suffix(".html"), target / "index.html"))
    return next((p for p in candidates if p.is_file()), target), unquote(parsed.fragment)

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    if not root.is_dir():
        print(f"ERROR: built site directory not found: {root}", file=sys.stderr)
        return 2
    files = sorted(root.rglob("*.html"))
    if not files:
        print(f"ERROR: no HTML files found under {root}", file=sys.stderr)
        return 2
    baseurl = read_baseurl()
    pages: dict[Path, LinkCollector] = {}
    for path in files:
        parser = LinkCollector()
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parser
    failures: list[str] = []
    for source, parser in pages.items():
        for attribute, raw in parser.targets:
            target, fragment = resolve_target(root, source, raw, baseurl)
            if target is None:
                continue
            if not target.is_file():
                failures.append(f"{source.relative_to(root)} -> {attribute}={raw} (target missing)")
                continue
            if attribute == "href" and fragment and target.suffix.lower() in {".html", ".htm"}:
                page = pages.get(target.resolve())
                if page is None:
                    page = LinkCollector()
                    page.feed(target.read_text(encoding="utf-8"))
                if fragment not in page.anchors:
                    failures.append(f"{source.relative_to(root)} -> {raw} (fragment #{fragment} missing)")
    if failures:
        print("Broken local links or fragments:")
        for failure in failures:
            print("  - " + failure)
        return 1
    print(f"Checked {len(files)} HTML files, local links/assets, and fragment targets; no broken targets found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
