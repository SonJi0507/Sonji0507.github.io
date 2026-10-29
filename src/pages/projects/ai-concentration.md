---
title: 우리AI 집중도 리포트 · 손지혁
description: 딥러닝 집중도 검사 결과를 보여주는 Django 웹 리포트. 손지혁은 홈의 감정·등급 표시와 베스트샷을 맡았습니다.
---

<section class="page-hero">
<p class="back"><a href="/projects/">프로젝트</a></p>
<p class="kicker">Team project · 2021</p>
<h1>우리AI 집중도 리포트</h1>
<p class="lede">딥러닝으로 본 집중도 검사 결과를 웹에서 읽는 리포트입니다. 모델이 돌려 준 값을 데이터베이스에 넣고, 그 값을 가져와 차트로 보여 줍니다.</p>
<p class="actions"><a href="https://github.com/SonJi0507/AI_Concentration" rel="noopener noreferrer">GitHub</a></p>
</section>

<section class="prose">
<h2>무엇을 만드나</h2>
<p>수업이나 학습 장면에서 측정한 집중도, 감정, 과목을 일별·주별로 보는 Django 웹 리포트입니다. 저장소 설명대로 딥러닝 코드는 이 프로젝트에 없습니다. SSD, CNN, Residual Masking Network의 결과는 DB에 있고, 웹은 그 결과를 시각화합니다.</p>

<h2>문제</h2>
<p>검사 숫자가 쌓여도, 홈에서 오늘의 감정과 등급을 바로 읽을 수 없으면 리포트가 아닙니다. 대표 장면(베스트샷)도 같은 화면에서 보여야 했습니다.</p>

<h2>역할</h2>
<p>팀 프로젝트의 웹 리포트에 참여했습니다. 2021년 10월에 홈의 감정 종류·등급 표시와 베스트샷을 구현했고, 그 커밋은 업스트림 저장소에 머지되었습니다. 차트 전반과 모델 연동은 팀의 작업입니다. 지금 공개된 제 포크는 업스트림과 같은 내용입니다.</p>

<h2>기술</h2>
<ul class="chips">
<li>Django</li>
<li>Python</li>
<li>MySQL</li>
<li>Chart.js</li>
<li>HTML</li>
<li>CSS</li>
<li>JavaScript</li>
</ul>

<h2>기술적으로 손댄 부분</h2>
<ul>
<li>홈 화면에서 감정 종류와 집중 등급이 보이게 뷰와 템플릿을 수정.</li>
<li>베스트샷을 고르고 홈에 붙이는 흐름을 <code>app/views.py</code>와 차트 템플릿에 추가.</li>
<li>집중 탭 템플릿에서 그 결과가 일별 뷰와 맞물리게 연결.</li>
<li>웹은 모델 추론을 하지 않고, 저장된 결과를 조회해 그리는 구조를 유지.</li>
</ul>
</section>
