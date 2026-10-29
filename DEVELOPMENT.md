# 개발

소스는 `src/`입니다. `make build`가 `dist/`를 만들고, 같은 파일을 레포 루트에도 복사합니다.

```bash
uv sync
make build
make serve   # http://127.0.0.1:8000
```

`dist/`는 gitignore입니다. 페이지는 `src/pages/`의 Markdown입니다. `index.md`는 그 폴더의 주소가 되고, 나머지 파일은 `/경로/`로 나갑니다.

`main` 푸시가 `.github/workflows/pages.yml`을 돌립니다. 배포 산출물은 `dist/`입니다.

`sonjh.com`을 Pages custom domain으로 붙이지 마세요. `CNAME`을 만들지 마세요.
