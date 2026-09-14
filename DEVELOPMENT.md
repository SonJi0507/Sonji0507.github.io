# 개발

소스는 `src/`입니다. `make build`가 `dist/`를 만들고, GitHub Jekyll 배포가 README를 홈으로 쓰지 않도록 같은 파일을 레포 루트(`index.html`, `about/`, `homelab/`, `css/`, `img/`)에도 복사합니다.

```bash
uv sync
make build
make serve   # http://127.0.0.1:8000
```

`dist/`는 gitignore입니다. 루트 HTML은 커밋합니다.

`main` 푸시가 `.github/workflows/pages.yml`을 돌립니다. GitHub 기본 워크플로 `pages-build-deployment`도 같이 돌며, 그게 README를 사이트로 렌더링하지 않게 루트 `index.html`이 필요합니다.

`sonjh.com`을 Pages custom domain으로 붙이지 마세요. `CNAME`을 만들지 마세요.
