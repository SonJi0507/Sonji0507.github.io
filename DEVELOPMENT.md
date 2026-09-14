# 개발

소스는 `src/`입니다. `make build`가 `dist/`를 만들고, 같은 파일을 레포 루트(`index.html`, `css/`, `img/`)에도 복사합니다.

```bash
uv sync
make build
make serve   # http://127.0.0.1:8000
```

`dist/`는 gitignore입니다. 한 페이지입니다. `src/pages/`에는 `index.md`만 둡니다.

`main` 푸시가 `.github/workflows/pages.yml`을 돌립니다.

`sonjh.com`을 Pages custom domain으로 붙이지 마세요. `CNAME`을 만들지 마세요.
