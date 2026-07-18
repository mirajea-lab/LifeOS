from abc import ABC, abstractmethod
from app.experience.models import Narrative

class BaseAnalyzer(ABC):
    @abstractmethod
    def analyze(self, narrative: Narrative):
        """Narrative 객체를 받아 분석 결과를 반환합니다."""
        pass