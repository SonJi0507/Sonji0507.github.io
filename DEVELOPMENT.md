# 개발

소스는 `src/`입니다. 프로젝트 본문은 `src/catalog.py`이고, `make build`가 `dist/`를 만든 뒤 같은 파일을 레포 루트에도 복사합니다.

```bash
uv sync
make build
make serve   # http://127.0.0.1:8000
make pdf     # assets/portfolio.pdf  (Chrome 또는 Chromium 필요)
```

`dist/`는 gitignore입니다. `make pdf`가 만든 `assets/portfolio.pdf`는 커밋합니다. 사이트 빌드는 그 파일을 `dist/assets/portfolio.pdf`로 복사해 `/assets/portfolio.pdf`에서 받게 합니다.

`main` 푸시가 `.github/workflows/pages.yml`을 돌립니다. 배포 산출물은 `dist/`입니다.

`sonjh.com`을 Pages custom domain으로 붙이지 마세요. `CNAME`을 만들지 마세요.
