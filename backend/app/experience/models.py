from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

# =====================================================================
# 0. 공통 하위 컴포넌트 및 타입 정의
# =====================================================================

class OriginType(str, Enum):
    """서사(Narrative)가 시작된 기원/맥락을 정의 (멀티모달 확장성 제공)"""
    DAILY_LOG = "daily_log"        # 사용자가 직접 작성한 일기/텍스트
    VOICE_MEMO = "voice_memo"      # 오디오 녹음 및 STT 변환 본
    PHOTO_MOMENT = "photo_moment"  # 사진 (EXIF, OCR, 비전 캡셔닝)
    DOCUMENT = "document"          # PDF, 웹스크랩, 책 구절
    BIO_METRIC = "bio_metric"      # 스마트워치 생체 신호 연동 등

class EmotionDetail(BaseModel):
    """경험에서 추출 및 추론된 감정의 정량적 상세"""
    name: str = Field(..., description="감정 명칭 (예: 성취감, 무력감, 감사)")
    intensity: int = Field(..., description="감정의 강도 (1~5 단계)")

class JourneyImpactDetail(BaseModel):
    """이 경험이 장기적인 인생 여정(Journey)에 미치는 서사적 영향"""
    area: str = Field(..., description="영향 영역 (예: 커리어, 자아실현, 대인관계)")
    description: str = Field(..., description="어떻게 삶의 궤적에 기여하는지에 대한 서술")


# =====================================================================
# 1단계: 원시 데이터 (Origin & Content)
# =====================================================================

class Narrative(BaseModel):
    """LifeOS로 들어오는 모든 가공되지 않은 사용자 경험 서사의 원형"""
    id: UUID = Field(default_factory=uuid4, description="서사 고유 식별 ID")
    origin: OriginType = Field(default=OriginType.DAILY_LOG, description="서사의 기원/발생 맥락")
    content: str = Field(..., description="원본 텍스트 내용 또는 멀티모달에서 추출한 텍스트")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, 
        description="Origin별 유동적 데이터 저장소 (예: GPS, 사진메타, 오디오길이)"
    )
    created_at: datetime = Field(default_factory=datetime.now, description="최초 발생/기록 시간")


# =====================================================================
# 2단계: AI 추론 레이어 (중간 결과물)
# =====================================================================

class AnalysisResult(BaseModel):
    """각 세부 에이전트들이 분석해낸 AI의 추론 및 임시 저장 데이터 레이어"""
    narrative_id: UUID = Field(..., description="대상 원본 Narrative ID")
    
    # 각 전용 Analyzer가 비동기/독립적으로 채워넣을 필드들
    facts: List[str] = Field(default_factory=list, description="FactAnalyzer 추출 결과")
    emotions: List[EmotionDetail] = Field(default_factory=list, description="EmotionAnalyzer 추론 결과")
    intent: Optional[str] = Field(None, description="IntentAnalyzer 추론 결과")
    reflection: Optional[str] = Field(None, description="ReflectionAnalyzer 생성 결과")
    related_people: List[str] = Field(default_factory=list, description="인물 관계 추출 결과")
    related_values: List[str] = Field(default_factory=list, description="핵심 가치 추출 결과")
    journey_impact: Optional[JourneyImpactDetail] = Field(None, description="JourneyAnalyzer 분석 결과")
    
    analyzed_at: datetime = Field(default_factory=datetime.now, description="AI 파이프라인 분석 완료 시간")


# =====================================================================
# 3단계: 시스템 확정본 (정합성 보장 서사 데이터)
# =====================================================================

class Experience(BaseModel):
    """AnalysisResult를 토대로 시스템 혹은 사용자가 검증하고 최종 확정한 완성형 서사 모델"""
    id: UUID = Field(default_factory=uuid4, description="최종 경험 데이터 고유 ID")
    narrative_id: UUID = Field(..., description="근간이 된 원본 Narrative ID")
    
    # 원본 Narrative의 주요 스냅샷 스토리지
    content: str = Field(..., description="원본 content 내용 복사본")
    created_at: datetime = Field(..., description="원본 최초 기록 시간")
    
    # 확정된 분석 서사 데이터 (최종 완료 단계이므로 모든 필드를 필수(Required)로 설정)
    facts: List[str] = Field(..., description="최종 확정된 객관적 사실들")
    emotions: List[EmotionDetail] = Field(..., description="최종 확정된 주관적 감정들")
    intent: str = Field(..., description="최종 확정된 행위의 내적 동기 및 의도")
    reflection: str = Field(..., description="최종 확정된 깨달음 및 성찰")
    related_people: List[str] = Field(..., description="최종 연관 인물")
    related_values: List[str] = Field(..., description="최종 자극/지향 가치")
    journey_impact: JourneyImpactDetail = Field(..., description="최종 확정된 Journey 영향")
    
    confirmed_at: datetime = Field(default_factory=datetime.now, description="시스템 최종 적재 시간")