.PHONY: build export-root serve qr pdf

# dist/ 에서 레포 루트로 복사하는 페이지 디렉터리.
PAGE_DIRS := projects portfolio

build:
	uv run python src/build.py
	$(MAKE) export-root

# 인쇄용 /portfolio/ 를 A4 PDF로 만든다. Chrome 또는 Chromium이 필요하다.
pdf: build
	uv run --with playwright python scripts/render_pdf.py
	mkdir -p dist/assets
	cp assets/portfolio.pdf dist/assets/portfolio.pdf

# GitHub의 pages-build-deployment(Jekyll)가 README를 홈으로 쓰지 않도록
# dist/ 를 레포 루트에도 둔다. Actions artifact와 같은 파일이다.
export-root:
	cp dist/index.html index.html
	cp dist/.nojekyll .nojekyll
	rm -rf css js img about homelab experience $(PAGE_DIRS)
	cp -R dist/css css
	if [ -d dist/js ]; then cp -R dist/js js; fi
	if [ -d dist/fonts ]; then rm -rf fonts && cp -R dist/fonts fonts; fi
	mkdir -p img
	if [ -d dist/img ]; then find dist/img -type f ! -name '.*' -exec cp {} img/ \;; fi
	for name in $(PAGE_DIRS); do \
	  if [ -d dist/$$name ]; then cp -R dist/$$name $$name; fi; \
	done

serve: build
	python3 -m http.server 8000 --directory dist

qr:
	uv run python main.py
