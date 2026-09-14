---
title: 홈서버
description: 집 Mac Mini 홈랩. Compose로 상태성 인프라를, Kubernetes로 웹앱을 돌립니다. 이 사이트는 GitHub Pages에서 서빙합니다.
---

# 홈서버

이 사이트는 GitHub Pages(`https://sonji0507.github.io`)에서 서빙합니다. 아래는 집 Mac Mini 홈랩의 실제 구성입니다. 그 클러스터에서 공개 앱 [`https://playground.sonjh.com`](https://playground.sonjh.com)이 Kubernetes Deployment로 동작 중입니다.

![홈랩 공개 경로. GitHub Pages는 이 사이트, Tunnel은 playground 앱, Compose는 Postgres·Redis·MinIO.](/img/homelab.svg)

이 HTML은 홈서버 Pod가 서빙하지 않습니다. 라이브 앱은 playground 한 줄뿐입니다.

## 왜 이렇게 나눴나

상태성 인프라(Postgres, Redis, MinIO, NPM, Tunnel)는 호스트 `docker-compose.yml`에 둡니다. 웹앱은 Colima Kubernetes의 `k8s/` 매니페스트로 올립니다. 데이터베이스는 오래 살고, 앱은 이미지 태그만 갈아끼우면 됩니다. 한 클러스터에 Postgres 오퍼레이터까지 올리면 싱글 노드 Mac Mini에서 운영 비용만 커집니다.

앱 코드와 배포 책임도 갈랐습니다. playground 레포는 `make image`만 하고, `oh-my-homeserver`는 Colima에 이미지를 실은 뒤 `kubectl set image`로 롤링합니다 (`k8s/DEPLOY.md`). 인프라 Makefile은 앱 빌드를 호출하지 않습니다. 이 포트폴리오 사이트는 그 경로를 쓰지 않습니다. 소스는 이 GitHub Pages 레포입니다.

## MinIO는 compose가 정본

MinIO는 `docker-compose.yml`에서 `infra-network`에 붙어 있고, 호스트로 API `:9000`과 콘솔 포트를 publish합니다. Pod는 `k8s/external/minio.yaml`의 ExternalName(`host.docker.internal:9000`)으로 API에만 붙습니다. `k8s/kustomization.yaml`이 이 서비스를 포함합니다.

README의 “MinIO는 infra-network에 붙지 않는다”, 매니페스트 주석의 같은 전제, MinIO.md의 “kustomize 미포함”은 compose·kustomize와 어긋납니다. 이 페이지는 파일을 따릅니다. 콘솔은 공개 프록시에 올리지 않습니다.

버킷과 Access Key는 compose가 만들지 않습니다. 앱을 붙일 때마다 `scripts/minio-onboard-app.sh`로 그 버킷만 허용하는 키를 발급하고, MinIO root 계정은 앱 env에 넣지 않습니다. 버킷은 private(`anonymous none`)입니다.

## 공개 면과 한계

playground Ingress(`k8s/apps/playground/ingress.yaml`)는 호스트 `playground.sonjh.com`만 보고, TLS 블록이 없습니다. 인증서는 Cloudflare와 NPM에서 끊고, 클러스터 안은 HTTP입니다. 이미지는 Colima의 Docker + cri-dockerd 경로로 load합니다. `nerdctl`/`k3s ctr` 실패는 이 구성에서 정상입니다.

인터넷에서 홈랩 앱으로 들어오는 길은 Cloudflare Tunnel입니다. 포트폴리오 자신은 Pages입니다. 노드는 Mac Mini 하나, Deployment replica는 1입니다.

| 결정 | 이유 |
| --- | --- |
| 상태성은 Compose, 웹앱은 k8s | 데이터는 호스트에 두고 앱만 자주 교체한다. |
| 앱 레포가 빌드, 인프라 레포가 배포 | `k8s/DEPLOY.md`. 레포를 섞지 않는다. |
| MinIO는 `infra-network` + 호스트 publish | `docker-compose.yml` 정본. Pod는 ExternalName `:9000`. |
| 앱별 버킷·Access Key | `minio-onboard-app.sh`. root 키는 앱에 없음. |
| TLS는 클러스터 밖 | Ingress에 cert-manager 없음. NPM/Cloudflare가 종료. |
| cri-dockerd load | Colima `runtime: docker`. nerdctl이 아님. |
| 공개 유입은 Tunnel, 이 사이트는 Pages | 정적 문서를 홈서버 장애에 묶지 않는다. |
| replica 1, 싱글 노드 | 집 장비. HA를 주장하지 않는다. |
