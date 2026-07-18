from uuid import UUID
from app.experience.models import Narrative, AnalysisResult, Experience, EmotionDetail, JourneyImpactDetail

# =====================================================================
# 세부 전문 부품 가상 분석기들 (Single Responsibility Principle)
# =====================================================================

class FactAnalyzer:
    def extract(self, content: str) -> list[str]:
        # TODO: 실제 LLM 프롬프트 및 인프라 연동
        return [f"'{content[:15]}...' 원문에서 육하원칙에 의거한 객관적 사실 추출"]

class EmotionAnalyzer:
    def infer(self, content: str) -> list[EmotionDetail]:
        # TODO: 감정 형용사 감지 및 스코어링 LLM 연동
        return [EmotionDetail(name="성취감", intensity=4)]

class IntentAnalyzer:
    def infer(self, content: str, facts: list[str]) -> str:
        # TODO: 행동의 이면 분석 LLM 연동
        return "사용자가 해당 행동을 유발하게 된 내면의 근본적인 목적 및 지향의도"

class ReflectionAnalyzer:
    def generate(self, content: str, intent: str) -> str:
        # TODO: 단순 요약이 아닌 가치 발견 및 깨달음 유도 생성 LLM 연동
        return "과거 컨텍스트 기반으로 도출된 입체적인 사후 평가 및 성찰 어시스트 문장"

class PeopleValueAnalyzer:
    def parse_network_and_values(self, content: str) -> tuple[list[str], list[str]]:
        # TODO: 엔티티(인명) 추출 및 라이프스타일 코어 가치 매핑 LLM 연동
        return ["가족", "동료"], ["성장", "연결"]

class JourneyAnalyzer:
    def analyze(self, intent: str, reflection: str) -> JourneyImpactDetail:
        # TODO: 장기 인생 마일스톤 및 맵 분석 연동
        return JourneyImpactDetail(
            area="자아실현 및 프로젝트 빌드",
            description="현재 진행 중인 LifeOS의 구조 설계 정교화를 통한 시스템 지속 가능성 기여"
        )


# =====================================================================
# 메인 오케스트레이터 (ExperienceAnalyzer)
# =====================================================================

class ExperienceAnalyzer:
    """각 하위 전문 Analyzer들을 총괄하여 Narrative를 AnalysisResult로 가공하는 총괄 감독관"""
    
    def __init__(self):
        # 각각의 전문 분석기 인스턴스를 소유
        self.fact_analyzer = FactAnalyzer()
        self.emotion_analyzer = EmotionAnalyzer()
        self.intent_analyzer = IntentAnalyzer()
        self.reflection_analyzer = ReflectionAnalyzer()
        self.people_value_analyzer = PeopleValueAnalyzer()
        self.journey_analyzer = JourneyAnalyzer()

    def analyze_narrative(self, narrative: Narrative) -> AnalysisResult:
        """Narrative 원본을 받아 조각조각 분석을 수행한 후 중간 결과 판(AnalysisResult)을 완성합니다."""
        
        # 1. 대상 내러티브 ID를 바인딩하여 빈 결과판 세팅
        result = AnalysisResult(narrative_id=narrative.id)
        
        # 2. 순차적 혹은 병렬적으로 각 에이전트 가동
        result.facts = self.fact_analyzer.extract(narrative.content)
        result.emotions = self.emotion_analyzer.infer(narrative.content)
        
        # 3. 의도(Intent) 분석가는 텍스트와 사실 정보를 결합하여 깊은 추론 진행
        result.intent = self.intent_analyzer.infer(narrative.content, result.facts)
        
        # 4. 인물 및 핵심 가치 발굴
        people, values = self.people_value_analyzer.parse_network_and_values(narrative.content)
        result.related_people = people
        result.related_values = values
        
        # 5. 의도와 서사 컨텍스트를 기반으로 깊이 있는 성찰 문장과 여정 임팩트 도출
        result.reflection = self.reflection_analyzer.generate(narrative.content, result.intent)
        result.journey_impact = self.journey_analyzer.analyze(result.intent, result.reflection)
        
        return result

    def finalize_experience(self, narrative: Narrative, result: AnalysisResult) -> Experience:
        """
        AI 분석 결과(AnalysisResult)를 바탕으로 예외가 없음을 검증하거나 
        사용자의 커스텀 수정 피드백을 수용하여 최종 시스템에 안착할 Experience 객체를 생성합니다.
        """
        # 이 단계에서 Optional 필드들이 누락되었는지 정합성을 검증한 뒤 객체를 조립합니다.
        return Experience(
            narrative_id=narrative.id,
            content=narrative.content,
            created_at=narrative.created_at,
            facts=result.facts,
            emotions=result.emotions,
            intent=result.intent or "해석 불가한 내적 동기",
            reflection=result.reflection or "추가적인 성찰이 필요합니다.",
            related_people=result.related_people,
            related_values=result.related_values,
            journey_impact=result.journey_impact or JourneyImpactDetail(area="미지", description="추후 추적 필요")
        )