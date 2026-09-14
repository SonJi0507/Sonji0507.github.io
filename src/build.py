#!/usr/bin/env python3
"""Jinja2 + Markdown → dist/ for GitHub Pages."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "src" / "pages"
TEMPLATES = ROOT / "src" / "templates"
STATIC = ROOT / "src" / "static"
DIST = ROOT / "dist"
CANONICAL_ORIGIN = "https://sonji0507.github.io"

IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def slugify(value: str, separator: str) -> str:
    value = str(value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    slug = re.sub(r"[-\s]+", separator, value).strip(separator)
    return slug or "section"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_meta(meta: dict, key: str, source: Path) -> str:
    value = meta.get(key)
    if value is None or not str(value).strip():
        fail(f"{source}: front matter '{key}' is required")
    return str(value).strip()


def check_images(body: str, source: Path) -> None:
    for url in IMG_RE.findall(body):
        if not url.startswith("/img/") or ".." in url or url.startswith("/img/../"):
            fail(
                f"{source}: image src must be root-absolute /img/... "
                f"(got {url!r})"
            )


def page_output(md_path: Path) -> tuple[Path, str]:
    rel = md_path.relative_to(PAGES)
    if rel.as_posix() == "index.md":
        return DIST / "index.html", "/"
    slug = rel.with_suffix("")
    return DIST / slug / "index.html", f"/{slug.as_posix()}/"


def canonical_href(path: str) -> str:
    if path == "/":
        return f"{CANONICAL_ORIGIN}/"
    return f"{CANONICAL_ORIGIN}{path}"


def render_pages(env: Environment) -> list[str]:
    template = env.get_template("base.html")
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc"],
        extension_configs={"toc": {"slugify": slugify}},
    )
    built: list[str] = []

    if not PAGES.is_dir():
        fail(f"missing pages dir: {PAGES}")

    for md_path in sorted(PAGES.rglob("*.md")):
        post = frontmatter.loads(md_path.read_text(encoding="utf-8"))
        if post.get("draft") is True:
            continue
        title = require_meta(post.metadata, "title", md_path)
        description = require_meta(post.metadata, "description", md_path)
        check_images(post.content, md_path)

        md.reset()
        body = md.convert(post.content)
        out_path, url_path = page_output(md_path)
        html = template.render(
            title=title,
            description=description,
            canonical=canonical_href(url_path),
            path=url_path,
            body=body,
        )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")
        built.append(url_path)

    if not built:
        fail("no pages built (all missing or draft)")
    return built


def copy_static() -> None:
    for name in ("css", "img"):
        src = STATIC / name
        dest = DIST / name
        if not src.is_dir():
            continue
        dest.mkdir(parents=True, exist_ok=True)
        for item in src.iterdir():
            if item.name.startswith("."):
                continue
            target = dest / item.name
            if item.is_file():
                shutil.copy2(item, target)


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html", "xml"]),
    )
    paths = render_pages(env)
    copy_static()

    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    if (DIST / "CNAME").exists():
        fail("dist/CNAME must not exist")

    print("built:")
    for path in paths:
        print(f"  {path}")


if __name__ == "__main__":
    main()
