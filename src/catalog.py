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
        "summary": "성경 구절의 연결을 그래프로 보여주는 웹 서비스입니다. 기획, 개발, 배포, 운영을 혼자 했습니다.",
        "description": "성경 구절의 연결을 그래프로 보여주고 QT 노트를 붙이는 웹 서비스 OurBibleNote.",
        "overview": "성경 구절이 서로를 가리키는 연결을 그래프로 보여 주는 웹 서비스입니다. 그 구절에 QT 노트를 붙이고, 연결된 다음 장으로 넘어갈 수 있습니다.",
        "problem": "구절 사이의 연결을 한 화면에서 보기 어려웠습니다. 역본을 바꿔도 같은 연결이 유지되어야 했고, 묵상 노트도 그 구절에 두고 싶었습니다.",
        "role": "기획, 개발, 배포, 운영을 혼자 맡았습니다.",
        "stack": ["Django", "DRF", "Python", "Next.js", "React", "TypeScript", "PostgreSQL", "Redis", "Docker", "GitHub Actions", "Playwright"],
        "points": [
            "백엔드는 Django 6와 Django REST Framework(Python 3.14)이고, 화면은 Next.js 15입니다. 둘을 한 Monorepo에 두었습니다.",
            "개역개정, 개역한글, NIV, NLT의 각 장을 그래프 노드로 두었습니다. 장과 장을 잇는 엣지, 태그, 그룹을 만들고 공유하는 API를 설계했습니다.",
            "Google, Kakao, Naver 로그인은 state 값으로 요청이 위조되지 않았는지 확인합니다. 로그인 상태는 Django 세션 쿠키로 유지합니다.",
            "Excel의 성경 본문을 Bible 테이블에 넣고, 이어서 그래프 노드를 만듭니다. 이 명령은 여러 번 실행해도 결과가 같습니다.",
            "GitHub Actions가 배포 전에 검사합니다. 백엔드는 ruff, ty, 마이그레이션 누락 검사, pytest이고, 화면은 lint, tsc, Vitest, Playwright E2E입니다. E2E는 허용되지 않은 스크립트(CSP 위반)가 0건인지 확인합니다.",
            "홈서버의 Docker Compose로 운영합니다. PostgreSQL 18, Redis, Reverse Proxy를 쓰고, 페이지마다 다른 nonce로 CSP를 적용해 허용하지 않은 스크립트를 막습니다.",
            "AI 코딩 도구가 따를 가이드를 두었습니다. 그 도구가 작성한 코드도 같은 CI 검사를 통과해야 합니다.",
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
        "summary": "집 Mac Mini에서 앱과 데이터를 나눠 운영합니다. 앱 Repository와 인프라 Repository를 분리하고, 외부에는 서비스만 엽니다.",
        "description": "집 Mac Mini에서 앱 Repository와 인프라 Repository를 분리해 배포하는 홈서버.",
        "overview": "집 Mac Mini에서 개인 인프라와 배포 환경을 직접 구축하고 운영합니다. 외부에는 서비스에 필요한 부분만 엽니다.",
        "problem": "PostgreSQL, Redis, 파일 Storage, Reverse Proxy는 자주 바꾸지 않습니다. 웹앱은 자주 바꿉니다. 그래서 데이터와 앱을 한곳에 두지 않았습니다.",
        "role": "인프라를 직접 구성하고 운영합니다. 인프라 Repository는 비공개입니다.",
        "stack": ["PostgreSQL", "Redis", "Docker", "Colima", "k3s", "Cloudflare", "Nginx Proxy Manager", "Beszel", "Uptime Kuma"],
        "points": [
            "PostgreSQL, Redis, 파일 Storage, Reverse Proxy는 Host의 Container로 둡니다. 웹앱은 Colima로 띄운 k3s에 올립니다.",
            "앱 Repository는 Container Image만 만듭니다. 비공개인 인프라 Repository가 그 Image를 k3s에 배포합니다.",
            "파일 Storage는 앱마다 접근 권한을 나눕니다. 관리자 계정은 앱에 넣지 않고, 관리 화면은 인터넷에 열지 않습니다.",
            "외부 앱은 공유기 포트를 열지 않습니다. Cloudflare Tunnel로 연결하고, TLS Termination은 Nginx Proxy Manager에서 합니다.",
            "머신과 Container 상태는 Beszel로 보고, 서비스가 떠 있는지는 Uptime Kuma로 확인합니다. 두 대시보드는 인터넷에 열지 않습니다.",
        ],
        "results": [
            "OurBibleNote를 이 구성 위에서 운영합니다.",
            "외부에 공개하는 서비스와 내부 관리 도구를 분리해, 대시보드와 관리 화면은 인터넷에 노출하지 않습니다.",
        ],
        "links": [],
        "diagram": True,
    },
]
