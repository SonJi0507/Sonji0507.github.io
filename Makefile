.PHONY: build export-root serve qr

build:
	uv run python src/build.py
	$(MAKE) export-root

# GitHub의 pages-build-deployment(Jekyll)가 README를 홈으로 쓰지 않도록
# dist/ 를 레포 루트에도 둔다. Actions artifact와 같은 파일이다.
export-root:
	cp dist/index.html index.html
	cp dist/.nojekyll .nojekyll
	rm -rf about homelab css img js
	test -d dist/about && cp -R dist/about about || true
	test -d dist/homelab && cp -R dist/homelab homelab || true
	cp -R dist/css css
	test -d dist/js && cp -R dist/js js || true
	mkdir -p img
	if [ -d dist/img ]; then find dist/img -type f ! -name '.*' -exec cp {} img/ \;; fi

serve: build
	python3 -m http.server 8000 --directory dist

qr:
	uv run python main.py
