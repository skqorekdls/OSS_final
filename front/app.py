# front/app.py

import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://backend:8000")

st.set_page_config(
    page_title="Deadline Survival Recommender",
    page_icon="⏰",
    layout="centered"
)

st.title("⏰ 대학생 과제 마감 생존 전략 추천 앱")
st.write("현재 과제 상황을 입력하면 FastAPI 백엔드가 추천 전략을 반환합니다.")

remaining_time = st.selectbox(
    "마감까지 남은 시간",
    ["3시간 이내", "하루 이내", "2~3일", "일주일 이상"]
)

progress = st.selectbox(
    "현재 진행 단계",
    ["아직 시작 안 함", "아이디어만 있음", "로컬 실행 완료", "Docker 실행 완료", "EC2 배포 완료"]
)

problem = st.selectbox(
    "가장 큰 문제 상황",
    ["아이디어 부족", "코드 구현", "Docker 오류", "EC2 배포 오류", "영상 촬영 부담"]
)

focus_time = st.slider("오늘 집중 가능한 시간", 1, 8, 3)

deploy_experience = st.radio(
    "EC2 배포 경험이 있나요?",
    ["있음", "없음"]
)

if st.button("추천 전략 받기"):
    payload = {
        "remaining_time": remaining_time,
        "progress": progress,
        "problem": problem,
        "focus_time": focus_time,
        "deploy_experience": deploy_experience
    }

    try:
        response = requests.post(f"{API_URL}/recommend", json=payload)
        response.raise_for_status()
        result = response.json()

        st.success("FastAPI 백엔드로부터 추천 결과를 받았습니다!")

        st.subheader("📌 추천 전략")
        st.write(result["strategy"])

        st.subheader("💬 추천 이유")
        st.write(result["recommendation"])

        st.subheader("🔥 위험도 점수")
        st.metric("Risk Score", result["risk_score"])

        st.subheader("✅ 체크리스트")
        for item in result["checklist"]:
            st.write(f"- {item}")

        st.caption(result["message"])

    except Exception as e:
        st.error("FastAPI 서버와 연결하지 못했습니다.")
        st.write(e)