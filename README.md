# Deadline Survival Recommender

## 1. 프로젝트 소개

이 프로젝트는 오픈소스소프트웨어실습 기말고사 대체 과제로 제작한
**Streamlit + FastAPI + Docker + AWS EC2 기반 추천 웹 애플리케이션**입니다.

사용자가 과제 마감까지 남은 시간, 현재 진행 상황, 문제 상황 등을 입력하면
Streamlit 프론트엔드가 FastAPI 백엔드에 요청을 보내고,
FastAPI는 입력값을 기반으로 과제 마감 생존 전략을 추천하여 JSON 형태로 반환합니다.

## 2. 프로젝트 주제

### 대학생 과제 마감 생존 전략 추천 앱

사용자의 현재 과제 진행 상황을 바탕으로 다음과 같은 결과를 추천합니다.

* 추천 전략
* 추천 이유
* 위험도 점수
* 실행 체크리스트

## 3. 주요 기능

* Streamlit을 이용한 사용자 입력 화면 구성
* FastAPI를 이용한 추천 API 구현
* Streamlit에서 FastAPI로 POST 요청 전송
* FastAPI의 JSON 응답을 Streamlit 화면에 출력
* Docker Compose를 이용한 프론트엔드/백엔드 컨테이너 실행
* AWS EC2 환경에서 웹 서비스 배포

## 4. 프로젝트 구조

```bash
final-recommend-app/
├── front/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── back/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## 5. 실행 방법

### 1) 저장소 클론

```bash
git clone [본인 GitHub Repository 주소]
cd final-recommend-app
```

### 2) Docker Compose로 실행

```bash
docker compose up --build -d
```

### 3) 실행 상태 확인

```bash
docker ps
```

## 6. 접속 주소

### Streamlit 프론트엔드

```bash
http://localhost:8501
```

EC2에서 실행하는 경우:

```bash
http://[EC2_PUBLIC_IP]:8501
```

### FastAPI 백엔드

```bash
http://localhost:8000
```

EC2에서 실행하는 경우:

```bash
http://[EC2_PUBLIC_IP]:8000
```

### FastAPI Swagger 문서

```bash
http://[EC2_PUBLIC_IP]:8000/docs
```

## 7. 서비스 동작 흐름

이 프로젝트의 핵심 동작 흐름은 다음과 같습니다.

```text
사용자 입력
→ Streamlit 프론트엔드
→ FastAPI 백엔드로 POST 요청
→ FastAPI에서 추천 결과 생성
→ JSON 응답 반환
→ Streamlit 화면에 추천 결과 출력
```

## 8. API 설명

### POST /recommend

사용자의 과제 상황 정보를 입력받아 추천 전략을 반환합니다.

#### 요청 예시

```json
{
  "remaining_time": "하루 이내",
  "progress": "아이디어만 있음",
  "problem": "Docker 오류",
  "focus_time": 3,
  "deploy_experience": "없음"
}
```

#### 응답 예시

```json
{
  "strategy": "최소 기능 구현 전략",
  "recommendation": "추천 로직을 단순화하고, Streamlit-FastAPI 연결과 Docker 실행 증명에 집중하세요.",
  "risk_score": 8,
  "checklist": [
    "FastAPI /recommend API 먼저 완성",
    "Streamlit에서 requests.post()로 연결",
    "docker-compose로 두 컨테이너 실행",
    "EC2에서 docker ps 화면 캡처",
    "영상에서 입력-추천-결과 흐름 설명"
  ],
  "message": "FastAPI에서 추천 결과를 생성했습니다."
}
```

## 9. 사용 기술

* Python
* Streamlit
* FastAPI
* Docker
* Docker Compose
* AWS EC2
* GitHub

## 10. 과제 요구사항 반영 내용

* Streamlit 프론트엔드에서 사용자 입력을 받음
* 추천 요청 버튼을 통해 FastAPI에 요청을 보냄
* FastAPI가 입력값을 받아 추천 결과를 생성함
* 추천 결과를 JSON 형태로 반환함
* Streamlit이 응답 결과를 받아 화면에 출력함
* Docker Compose를 통해 프론트엔드와 백엔드를 각각 컨테이너로 실행함
* AWS EC2 환경에서 외부 접속 가능한 형태로 배포함
