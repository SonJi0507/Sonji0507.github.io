# sonji0507.github.io

백엔드 포트폴리오. Canonical URL은 `https://sonji0507.github.io` 입니다.
소스는 `src/`, 게시는 GitHub Pages Actions가 `dist/` artifact로 합니다.

이 사이트는 홈서버에서 호스팅하지 않습니다. 홈랩 설명은 `/homelab/`에 둡니다.

## 로컬

```bash
uv sync
make build          # src/ → dist/
make serve          # http://127.0.0.1:8000
```

`dist/`는 gitignore입니다. 루트에 HTML을 커밋하지 마세요.

## 배포

`main` 푸시가 `.github/workflows/pages.yml`을 돌립니다.

**머지 직후 한 번 (git 밖):**

1. Repo **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 바꿉니다.
2. `sonjh.com`을 Pages custom domain으로 붙이지 않습니다. `CNAME` 파일을 만들지 않습니다.

성공하면 `https://sonji0507.github.io`에 스텁이 뜹니다.

QR 헬퍼: `make qr` (`main.py`, URL은 github.io 유지).
