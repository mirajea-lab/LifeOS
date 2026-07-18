# Architecture Decision Records (ADR)

LifeOS에서 중요한 설계 결정들을 기록한다.

---

# ADR-001

## 제목

Memory 대신 Experience를 사용한다.

## 이유

Memory는 저장 중심의 개념이다.

하지만 사람은 사건을 기억하는 것이 아니라

감정과 의미가 담긴 경험을 기억한다.

LifeOS는 기억 저장소가 아니라

경험을 이해하는 시스템을 목표로 한다.

---

# ADR-002

## 제목

Journey를 핵심 개념으로 채택한다.

## 이유

Experience는 개별 사건이다.

Journey는 Experience들이 연결되어 만들어지는 삶이다.

LifeOS는 사용자의 Journey를 이해하는 AI를 목표로 한다.

---

# ADR-003

## 제목

Narrative를 입력 모델로 사용한다.

## 이유

사용자는 Experience를 입력하지 않는다.

사용자는 이야기를 입력한다.

AI는 Narrative를 Experience로 해석한다.

Narrative는 모든 분석의 시작점이다.

---

# ADR-004

## 제목

Analyzer를 역할별로 분리한다.

## 이유

AI에게 하나의 거대한 프롬프트를 전달하는 것보다

역할별 Analyzer를 분리하는 것이

품질과 유지보수 측면에서 유리하다.

현재 Analyzer

- Fact Analyzer
- Emotion Analyzer
- Intent Analyzer
- Reflection Analyzer
- Journey Analyzer

ExperienceAnalyzer는

각 Analyzer를 조율하는 Orchestrator 역할만 수행한다.

---

# ADR-005

## 제목

Narrative는 다양한 Source를 지원한다.

## 이유

LifeOS는 텍스트 메모 앱이 아니다.

입력은 앞으로

- Text
- Voice
- Photo
- PDF
- Email
- Calendar
- Chat

등으로 확장될 수 있다.

---

# ADR-006

## 제목

Confidence를 저장한다.

## 이유

AI는 항상 정답을 말하지 않는다.

따라서

모든 추론에는 Confidence가 포함되어야 한다.

사용자는 이를 수정할 수 있으며

LifeOS는 사용자 피드백을 통해

더 정확한 Experience를 만들어간다.

---

# ADR-007

## 제목

철학을 코드보다 먼저 설계한다.

## 이유

LifeOS는 기술 프로젝트가 아니다.

철학

↓

도메인

↓

아키텍처

↓

인터페이스

↓

구현

↓

기술

의 순서를 따른다.

이 원칙은 프로젝트 전체에서 유지한다.