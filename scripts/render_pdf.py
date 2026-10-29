#!/usr/bin/env python3
"""Render dist/portfolio/ to assets/portfolio.pdf with headless Chrome.

Requires Google Chrome (or Chromium) and Playwright:

    uv run --with playwright python scripts/render_pdf.py

`make pdf` builds the site first, then runs this script.
"""

from __future__ import annotations

import shutil
import sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PDF = ROOT / "assets" / "portfolio.pdf"
PORT = 8765


def chrome_channel() -> str:
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        if shutil.which(name):
            return "chrome" if "chrome" in name else "chromium"
    sys.exit("error: install Google Chrome or Chromium, then re-run make pdf")


def main() -> None:
    if not (DIST / "portfolio" / "index.html").is_file():
        sys.exit("error: dist/portfolio/index.html missing. run make build first")

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(DIST), **kwargs)

        def log_message(self, format: str, *args) -> None:  # noqa: A003
            return

    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        server.shutdown()
        sys.exit("error: pip install playwright, or run via: uv run --with playwright python scripts/render_pdf.py")

    url = f"http://127.0.0.1:{PORT}/portfolio/"
    PDF.parent.mkdir(parents=True, exist_ok=True)
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel=chrome_channel(), headless=True)
            page = browser.new_page()
            page.emulate_media(media="print")
            page.goto(url, wait_until="networkidle")
            page.evaluate("() => document.fonts.ready")
            page.pdf(
                path=str(PDF),
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
            browser.close()
    finally:
        server.shutdown()

    bundled = DIST / "assets" / "portfolio.pdf"
    bundled.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PDF, bundled)
    print(f"wrote {PDF.relative_to(ROOT)} ({PDF.stat().st_size} bytes)")


if __name__ == "__main__":
    main()