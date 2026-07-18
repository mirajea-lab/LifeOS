# Concepts

LifeOS에서 사용되는 핵심 개념들을 정의한다.

---

# Narrative

사용자가 AI에게 전달하는 원본 이야기(Raw Story).

Narrative는 아직 AI가 해석하지 않은 상태이다.

입력 형태는 다양할 수 있다.

- Text
- Voice
- Photo
- PDF
- Email
- Calendar
- Chat
- 기타 다양한 Source

Narrative는 Experience의 재료가 된다.

---

# Experience

AI가 Narrative를 분석하여 생성한 하나의 경험.

Experience는 단순한 메모가 아니다.

Experience는 다음 요소들을 포함한다.

- Fact
- Emotion
- Intent
- Reflection
- Journey Impact

Experience는 LifeOS에서 가장 중요한 도메인 모델이다.

---

# Fact

Narrative 안에서 실제 발생한 사실.

예)

- 아내와 장을 봤다.
- 큰딸과 소꿉놀이를 했다.
- 운동을 했다.

Fact는 AI의 해석이 아니라 가능한 한 객관적인 정보이다.

---

# Emotion

Narrative 속에서 느껴지는 감정.

예)

- 기쁨
- 허무함
- 설렘
- 아련함
- 답답함

Emotion은 AI의 추론 결과이며 Confidence를 가진다.

---

# Intent

사용자가 왜 그런 행동을 했는가에 대한 추론.

예)

- 변하고 싶었다.
- 가족과 시간을 보내고 싶었다.
- 도전하고 싶었다.

Intent는 행동보다 더 깊은 동기를 의미한다.

---

# Reflection

사용자가 경험을 통해 얻은 생각.

Reflection은 AI가 생성할 수도 있고
사용자가 직접 수정할 수도 있다.

---

# Journey

Experience들이 시간에 따라 연결되어 만들어지는 삶의 흐름.

Journey는 하나의 사건이 아니라

사용자가 어떤 사람이 되어가는 과정이다.

---

# Relation

Experience와 Experience,

Experience와 Person,

Experience와 Memory,

Experience와 Value를 연결하는 관계.

LifeOS는 데이터를 저장하는 시스템이 아니라

관계를 저장하는 시스템이다.

---

# Person

사용자의 삶에 영향을 주는 사람.

예)

- 가족
- 친구
- 직장동료
- 교회 사람들

Experience는 여러 Person과 연결될 수 있다.

---

# Timeline

Experience가 시간순으로 연결된 구조.

Journey를 시각적으로 표현하는 기반이 된다.

---

# Confidence

AI가 자신의 분석 결과를 얼마나 확신하는지 나타내는 값.

예)

Emotion
0.92

Intent
0.64

Reflection
0.88

Confidence는 사용자 수정 및 재분석의 기준이 된다.

---

# AnalysisResult

Analyzer가 생성하는 중간 결과.

Narrative

↓

AnalysisResult

↓

Experience

AI의 추론 결과와

사용자가 최종 확정한 Experience를 분리하기 위해 존재한다.