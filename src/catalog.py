"""Public portfolio projects. Facts stay inside the vetted career note."""

SITE = {
    "name": "손지혁",
    "role": "백엔드 개발자",
    "role_en": "Backend Developer",
    "summary": "빠르게 배우고 바로 적용하는 백엔드 개발자입니다.",
    "email": "jhson0507@gmail.com",
    "github": "https://github.com/SonJi0507",
    "github_label": "github.com/SonJi0507",
    "site": "https://sonji0507.github.io",
}

PROJECTS = [
    {
        "slug": "our-bible-note",
        "kicker": "사이드 프로젝트",
        "when": "운영 중",
        "title": "OurBibleNote",
        "summary": "성경 구절의 관계를 그래프로 보고 QT 노트를 잇는 웹 서비스. 기획부터 운영까지 혼자 맡았습니다.",
        "description": "성경 구절의 관계를 그래프로 보고 QT 노트를 잇는 웹 서비스 OurBibleNote.",
        "overview": "성경 구절 간의 관계를 그래프로 시각화하고 QT 노트를 연결하는 웹 서비스입니다. 구약과 신약을 한 장의 지도로 보고, 연결된 장을 따라 읽으며 그룹과 묵상 노트를 남깁니다.",
        "problem": "성경은 구절이 서로를 가리키는데, 그 관계를 한 장의 지도로 보면서 묵상 노트까지 같은 자리에 두기가 어려웠습니다. 역본을 바꿔도 같은 자리가 이어져야 했습니다.",
        "role": "혼자 기획부터 개발, 배포, 운영까지 맡았습니다.",
        "stack": ["Django", "DRF", "Python", "Next.js", "React", "TypeScript", "PostgreSQL", "Redis", "Docker", "GitHub Actions", "Playwright"],
        "points": [
            "Django 6 + DRF 백엔드(Python 3.14, uv)와 Next.js 15(App Router, React 19, TypeScript) 프론트엔드를 한 모노레포로 구성했습니다.",
            "성경 4개 역본(개역개정·개역한글·NIV·NLT)을 장 단위 그래프 노드로 구성하고, 노드·엣지·태그·그룹 공유 API를 설계했습니다.",
            "Google·Kakao·Naver 소셜 로그인은 state 검증과 Django 세션 쿠키로 인증합니다.",
            "데이터 시딩은 멱등합니다. Excel에서 Bible 테이블을 거쳐 그래프 노드까지 이어집니다.",
            "GitHub Actions에서 ruff·ty·마이그레이션 누락 검사·pytest(PostgreSQL)와 프론트 lint·tsc·Vitest·Playwright E2E를 돌립니다. E2E는 CSP 위반 0건을 확인합니다.",
            "홈서버에 Docker Compose로 운영합니다. PostgreSQL 18, Redis, 리버스 프록시, nonce 기반 CSP를 씁니다.",
            "에이전트용 가이드를 두고, lint·타입 검사·테스트·E2E를 CI로 강제해 도구가 작성한 코드도 같은 기준으로 검증합니다.",
        ],
        "results": [
            "https://ourbiblenote.com 에서 운영 중입니다.",
            "배포 전에 lint, 타입 검사, pytest, E2E가 통과해야 합니다.",
        ],
        "links": [{"label": "ourbiblenote.com", "href": "https://ourbiblenote.com"}],
        "diagram": False,
    },
    {
        "slug": "homelab",
        "kicker": "개인 인프라",
        "when": "진행 중",
        "title": "홈서버",
        "summary": "집 Mac Mini에서 데이터와 앱의 수명을 나누고, 공개할 면만 밖으로 열어 서비스를 올립니다.",
        "description": "집 Mac Mini로 개인 인프라와 배포를 직접 돌리는 홈서버.",
        "overview": "집 Mac Mini로 개인 인프라와 배포를 직접 돌리는 작업입니다. 클라우드 콘솔을 흉내 내는 대신, 앱을 올렸다 내리고 저장소를 나누고 공개 면만 밖으로 냅니다.",
        "problem": "데이터베이스, 캐시, 파일 저장소, 프록시처럼 오래 남는 것과 자주 갈아끼우는 웹앱의 수명이 다릅니다. 데이터는 잘 안 건드리고 앱만 자주 바꾸고 싶었습니다.",
        "role": "개인 인프라를 직접 구성하고 운영합니다. 인프라 저장소는 공개하지 않습니다.",
        "stack": ["PostgreSQL", "Redis", "Docker", "Colima", "k3s", "Cloudflare", "Nginx Proxy Manager", "Beszel", "Uptime Kuma"],
        "points": [
            "오래 남는 것은 호스트 위 컨테이너로 두고, 웹앱은 Colima로 띄운 k3s에 올립니다.",
            "앱 저장소는 컨테이너 이미지만 만들고, 인프라 저장소가 그 이미지를 받아 올립니다.",
            "파일 저장소는 앱마다 접근 권한을 나눕니다. 관리자 계정은 앱에 넣지 않고, 관리 화면은 인터넷에 열지 않습니다.",
            "밖에 내보내는 앱은 공유기 포트를 열지 않고 Cloudflare Tunnel로 나갑니다. 인증서는 Nginx Proxy Manager에서 끊습니다.",
            "머신과 컨테이너 상태는 Beszel로, 서비스가 살아 있는지는 Uptime Kuma로 봅니다. 대시보드는 밖에 열지 않습니다.",
        ],
        "results": [
            "OurBibleNote를 이 구성 위에서 운영합니다.",
            "공개 면과 관리 면을 나눠, 대시보드와 관리 화면은 인터넷에 열지 않습니다.",
        ],
        "links": [],
        "diagram": True,
    },
]
