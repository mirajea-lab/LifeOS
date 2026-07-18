from app.ai.analyzers.base import BaseAnalyzer
from app.experience.models import Narrative, EmotionAnalysis

class EmotionAnalyzer(BaseAnalyzer):
    def analyze(self, narrative: Narrative) -> EmotionAnalysis:
        # Step 3 목표: 아직 GPT 없이 구조만 잡기 때문에 빈 데이터나 기본 뼈대만 반환
        return EmotionAnalysis(facts=[], confidence=1.0)    