# back/main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Deadline Survival Recommender API")

class RecommendRequest(BaseModel):
    remaining_time: str
    progress: str
    problem: str
    focus_time: int
    deploy_experience: str

@app.get("/")
def home():
    return {"message": "FastAPI backend is running"}

@app.post("/recommend")
def recommend(data: RecommendRequest):
    risk_score = 0

    if data.remaining_time in ["하루 이내", "3시간 이내"]:
        risk_score += 3
    elif data.remaining_time == "2~3일":
        risk_score += 2
    else:
        risk_score += 1

    if data.progress in ["아직 시작 안 함", "아이디어만 있음"]:
        risk_score += 3
    elif data.progress == "로컬 실행 완료":
        risk_score += 1

    if data.problem in ["Docker 오류", "EC2 배포 오류"]:
        risk_score += 2

    if data.focus_time < 2:
        risk_score += 2

    if data.deploy_experience == "없음":
        risk_score += 1

    if risk_score >= 8:
        strategy = "최소 기능 구현 전략"
        recommendation = "추천 로직을 단순화하고, Streamlit-FastAPI 연결과 Docker 실행 증명에 집중하세요."
        checklist = [
            "FastAPI /recommend API 먼저 완성",
            "Streamlit에서 requests.post()로 연결",
            "docker-compose로 두 컨테이너 실행",
            "EC2에서 docker ps 화면 캡처",
            "영상에서 입력-추천-결과 흐름 설명"
        ]
    elif risk_score >= 5:
        strategy = "안정 구현 전략"
        recommendation = "기능을 너무 늘리지 말고, UI와 결과 설명을 보기 좋게 다듬는 방향이 좋습니다."
        checklist = [
            "입력 항목 4~5개 구성",
            "추천 결과에 이유 포함",
            "FastAPI docs 접속 확인",
            "README에 실행 방법 작성"
        ]
    else:
        strategy = "완성도 강화 전략"
        recommendation = "기본 기능이 안정적이라면 결과 카드, 위험도 표시, README 정리를 강화하세요."
        checklist = [
            "추천 결과 디자인 개선",
            "예외 처리 추가",
            "GitHub README 정리",
            "데모 영상 시나리오 준비"
        ]

    return {
        "strategy": strategy,
        "recommendation": recommendation,
        "risk_score": risk_score,
        "checklist": checklist,
        "message": "FastAPI에서 추천 결과를 생성했습니다."
    }