---
title: Sonji
description: 백엔드·플랫폼. 홈서버 미니 프로젝트를 진행 중입니다.
---

<section class="project" id="homeserver">
<p class="kicker">Mini project · 진행 중</p>
<h1>홈서버</h1>
<p class="reveal">집 Mac Mini로 개인 인프라와 배포를 직접 돌리는 작업입니다. 클라우드 콘솔을 흉내 내는 게 아니라, 앱을 올렸다 내리고 저장소를 나누고 공개 면만 밖으로 내는 일을 실제로 굴려 보는 중입니다.</p>
<p class="reveal">오래 남는 것(데이터베이스, 캐시, 파일 저장소, 프록시)은 호스트 위의 컨테이너로 묶어 두고, 웹앱은 Colima로 띄운 k3s에 올립니다. 데이터는 잘 안 건드리고 앱만 자주 갈아끼우려고 나눈 구성입니다.</p>
<p class="reveal">앱 저장소는 컨테이너 이미지만 만들고, 인프라 저장소가 그 이미지를 받아 올립니다. 역할을 한 레포에 섞지 않습니다.</p>
<p class="reveal">파일 저장소는 앱마다 열쇠를 따로 줍니다. 관리자 계정은 앱에 넣지 않고, 관리 화면은 인터넷에 열지 않습니다.</p>
<p class="reveal">밖에 내보내는 앱은 공유기 포트를 열지 않고 Cloudflare Tunnel로 나갑니다. 앞에서 Nginx Proxy Manager가 인증서를 끊고, 그 뒤에 배포된 웹앱이 돌아가고 있습니다.</p>
<p class="reveal">머신과 컨테이너 상태는 Beszel로, 배포한 서비스가 살아 있는지는 Uptime Kuma로 봅니다. 대시보드는 밖에 열지 않습니다.</p>

<img class="reveal" src="/img/homelab.svg" alt="배포된 앱은 Cloudflare Tunnel과 Nginx Proxy Manager를 거쳐 Colima k3s로 간다. 데이터는 호스트 컨테이너에 남고, Beszel과 Uptime Kuma로 상태를 본다.">
</section>

<section class="stack reveal" id="stack">
<p class="kicker">Using</p>
<ul class="chips">
<li>Python</li>
<li>Django</li>
<li>FastAPI</li>
<li>PostgreSQL</li>
<li>Redis</li>
<li>Docker</li>
<li>Colima</li>
<li>k3s</li>
<li>Cloudflare</li>
<li>Nginx Proxy Manager</li>
<li>Terraform</li>
<li>Beszel</li>
<li>Uptime Kuma</li>
</ul>
</section>
