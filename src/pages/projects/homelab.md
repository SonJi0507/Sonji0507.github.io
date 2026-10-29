---
title: 홈서버 · 손지혁
description: 집 Mac Mini로 개인 인프라와 배포를 직접 돌리는 홈서버. 데이터와 앱을 나누고, 공개 면만 밖으로 냅니다.
---

<section class="page-hero">
<p class="back"><a href="/projects/">프로젝트</a></p>
<p class="kicker">Mini project · 진행 중</p>
<h1>홈서버</h1>
<p class="lede">집 Mac Mini로 개인 인프라와 배포를 직접 돌리는 작업입니다. 클라우드 콘솔을 흉내 내는 게 아니라, 앱을 올렸다 내리고 저장소를 나누고 공개 면만 밖으로 내는 일을 실제로 굴려 보는 중입니다.</p>
</section>

<section class="prose">
<h2>문제</h2>
<p>오래 남는 것(데이터베이스, 캐시, 파일 저장소, 프록시)과 자주 갈아끼우는 웹앱의 수명이 다릅니다. 데이터는 잘 안 건드리고 앱만 자주 바꾸려고 둘을 나눴습니다.</p>

<h2>역할</h2>
<p>개인 인프라를 직접 구성하고 운영합니다. 인프라 저장소는 비공개라 여기에 링크하지 않습니다. <a href="/projects/our-bible-note/">OurBibleNote</a>도 이 위에서 돌아갑니다.</p>

<h2>구성</h2>
<p>오래 남는 것은 호스트 위의 컨테이너로 묶어 두고, 웹앱은 Colima로 띄운 k3s에 올립니다.</p>
<p>앱 저장소는 컨테이너 이미지만 만들고, 인프라 저장소가 그 이미지를 받아 올립니다. 역할을 한 레포에 섞지 않습니다.</p>
<p>파일 저장소는 앱마다 접근 권한을 나눕니다. 관리자 계정은 앱에 넣지 않고, 관리 화면은 인터넷에 열지 않습니다.</p>
<p>밖에 내보내는 앱은 공유기 포트를 열지 않고 Cloudflare Tunnel로 나갑니다. 앞에서 Nginx Proxy Manager가 인증서를 끊고, 그 뒤에 배포된 웹앱이 돌아가고 있습니다.</p>
<p>머신과 컨테이너 상태는 Beszel로, 배포한 서비스가 살아 있는지는 Uptime Kuma로 봅니다. 대시보드는 밖에 열지 않습니다.</p>

<img src="/img/homelab.svg" alt="배포된 앱은 Cloudflare Tunnel과 Nginx Proxy Manager를 거쳐 Colima k3s로 간다. 데이터는 호스트 컨테이너에 남고, Beszel과 Uptime Kuma로 상태를 본다.">

<h2>기술</h2>
<ul class="chips">
<li>PostgreSQL</li>
<li>Redis</li>
<li>Docker</li>
<li>Colima</li>
<li>k3s</li>
<li>Cloudflare</li>
<li>Nginx Proxy Manager</li>
<li>Beszel</li>
<li>Uptime Kuma</li>
</ul>
</section>
