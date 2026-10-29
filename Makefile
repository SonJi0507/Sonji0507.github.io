.PHONY: build export-root serve qr

# dist/ 에서 레포 루트로 복사하는 페이지 디렉터리.
PAGE_DIRS := experience projects

build:
	uv run python src/build.py
	$(MAKE) export-root

# GitHub의 pages-build-deployment(Jekyll)가 README를 홈으로 쓰지 않도록
# dist/ 를 레포 루트에도 둔다. Actions artifact와 같은 파일이다.
export-root:
	cp dist/index.html index.html
	cp dist/.nojekyll .nojekyll
	rm -rf css js img about homelab $(PAGE_DIRS)
	cp -R dist/css css
	if [ -d dist/js ]; then cp -R dist/js js; fi
	mkdir -p img
	if [ -d dist/img ]; then find dist/img -type f ! -name '.*' -exec cp {} img/ \;; fi
	for name in $(PAGE_DIRS); do \
	  if [ -d dist/$$name ]; then cp -R dist/$$name $$name; fi; \
	done

serve: build
	python3 -m http.server 8000 --directory dist

qr:
	uv run python main.py
