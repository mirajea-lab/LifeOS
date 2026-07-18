from datetime import datetime
from fastapi import FastAPI
from app.experience.models import Narrative, Experience
from app.ai.analyzers.experience_analyzer import ExperienceAnalyzer

# 1. FastAPI 인스턴스 생성 (uvicorn이 이 'app'을 바라보게 됩니다)
app = FastAPI(title="LifeOS AI Engine", version="1.0")

# 2. 오케스트레이터는 서버가 켜질 때 한 번만 생성해서 재사용합니다.
analyzer = ExperienceAnalyzer()


@app.get("/")
def read_root():
    """서버 생존 확인용 홈 엔드포인트"""
    return {"status": "ok", "message": "LifeOS AI 뼈대 서버 가동 중"}


@app.post("/analyze", response_model=Experience)
def analyze_narrative(user_input: Narrative):
    """
    사용자의 서사(Narrative)를 받아 AI 뼈대 구조(Experience)로 분석 및 조립합니다.
    """
    # 사용자가 created_at을 안 보냈을 경우를 대비한 기본값 보정 (선택 사항)
    if not user_input.created_at:
        user_input.created_at = datetime.now()
        
    # 오케스트레이터 가동
    experience_result = analyzer.analyze(user_input)
    
    # 최종 조립된 Experience 객체 반환 (FastAPI가 알아서 JSON으로 변환해 줍니다)
    return experience_result