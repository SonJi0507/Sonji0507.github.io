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
            "개인 웹 서비스를 이 구성 위에서 운영합니다.",
            "외부에 공개하는 서비스와 내부 관리 도구를 분리해, 대시보드와 관리 화면은 인터넷에 노출하지 않습니다.",
        ],
        "links": [],
        "diagram": True,
    },
]
