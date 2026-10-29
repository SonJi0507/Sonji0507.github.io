# 손지혁

백엔드 개발자 포트폴리오입니다. [GitHub Pages](https://sonji0507.github.io).

소개, 프로젝트, 연락, 제출용 PDF를 정적 페이지로 빌드합니다. 로컬 빌드는 [DEVELOPMENT.md](DEVELOPMENT.md)를 보세요.

## PDF

Chrome 또는 Chromium이 설치된 상태에서:

```bash
make pdf
```

`assets/portfolio.pdf`를 만들고, 사이트에서는 `/assets/portfolio.pdf`로 받습니다. `make pdf`는 `make build` 뒤에 Playwright로 `/portfolio/`를 A4로 인쇄합니다.
