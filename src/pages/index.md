---
title: Sonji
description: 백엔드·플랫폼. 집에서 서버를 굴리는 미니 프로젝트를 진행 중입니다.
---

<section class="hero">
<p class="kicker">Backend · Platform</p>
<h1>집에서 서버를 굴립니다.</h1>
<p class="lede">백엔드와 배포를 만듭니다. 지금은 집 서버를 직접 올리는 일을 하고 있습니다.</p>
</section>

<section class="project" id="homeserver">
<p class="kicker reveal">Mini project · 진행 중</p>
<h2 class="reveal">홈서버</h2>
<p class="reveal">집 Mac Mini로 개인 인프라와 배포를 직접 돌리는 작업입니다. 클라우드 콘솔을 흉내 내는 게 아니라, 앱을 올렸다 내리고 저장소를 나누고 공개 면만 밖으로 내는 일을 실제로 굴려 보는 중입니다.</p>
<p class="reveal">오래 남는 것(데이터베이스, 캐시, 파일 저장소, 프록시)은 호스트 위의 컨테이너로 묶어 두고, 웹앱만 쿠버네티스에 올립니다. 데이터는 잘 안 건드리고 앱만 자주 갈아끼우려고 나눈 구성입니다.</p>
<p class="reveal">앱 저장소는 컨테이너 이미지만 만들고, 인프라 저장소가 그 이미지를 받아 올립니다. 역할을 한 레포에 섞지 않습니다.</p>
<p class="reveal">파일 저장소는 앱마다 열쇠를 따로 줍니다. 관리자 계정은 앱에 넣지 않고, 관리 화면은 인터넷에 열지 않습니다.</p>
<p class="reveal">밖에 내보내는 앱은 공유기 포트를 열지 않고 터널로 나갑니다. 인증서는 클러스터 밖에서 끊고, 그 위에 배포된 웹앱이 돌아가고 있습니다.</p>
<p class="reveal">머신과 컨테이너 상태는 Beszel로, 배포한 서비스가 살아 있는지는 Uptime Kuma로 봅니다. 대시보드는 밖에 열지 않습니다.</p>

<img class="reveal" src="/img/homelab.svg" alt="배포된 앱은 터널과 프록시를 거쳐 쿠버네티스로 간다. 데이터는 호스트 컨테이너에 남고, Beszel과 Uptime Kuma로 상태를 본다.">

<ul class="points">
<li class="reveal"><strong>상태와 앱을 나눔</strong> 데이터는 호스트에 두고, 웹앱만 클러스터에서 갈아끼웁니다.</li>
<li class="reveal"><strong>빌드와 배포를 나눔</strong> 앱은 이미지만 만들고, 인프라가 올려서 교체합니다.</li>
<li class="reveal"><strong>열쇠는 앱 단위</strong> 저장소 루트 키를 앱에 넣지 않습니다.</li>
<li class="reveal"><strong>공개 면을 좁힘</strong> 배포된 앱만 터널로 내보냅니다. 관리 도구는 밖에 없습니다.</li>
<li class="reveal"><strong>상태를 봄</strong> 호스트는 Beszel, 서비스 업타임은 Uptime Kuma. 화면은 공개하지 않습니다.</li>
</ul>
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
<li>Kubernetes</li>
<li>Terraform</li>
<li>Beszel</li>
<li>Uptime Kuma</li>
</ul>
</section>
