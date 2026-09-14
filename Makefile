.PHONY: build serve qr

build:
	uv run python src/build.py

serve: build
	python3 -m http.server 8000 --directory dist

qr:
	uv run python main.py
