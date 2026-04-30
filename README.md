# 🚀 Prompt Optimizer

A cli tool that optimizes the tokens with AI prompt
ChatGPT, Claude 등으로 보내기 전에 프롬프트를 더 간결하고 명확하게 만들어줍니다.

## ✨ 기능

- 📊 **토큰 개수 계산** - 원본과 최적화된 프롬프트의 토큰 수 비교
- ✨ **자동 최적화** - 규칙 기반 최적화 엔진
- 🔄 **Before/After 비교** - 시각적으로 개선 사항 확인
- 💾 **파일 입력 지원** - 파일에서 프롬프트 읽기
- 🎯 **대화형 모드** - 여러 번 최적화 가능

## 🎯 최적화 규칙

- ✂️ 불필요한 완곡 표현 제거 (please, kindly, could you 등)
- 🗑️ 감사 표현 제거 (thank you, thanks 등)
- 🎨 과장 표현 정리 (very, really, just 등)
- 🔄 동의어를 더 간단한 표현으로 교체
- 📐 구조 및 띄어쓰기 개선

## 📦 설치

### 요구사항
- Python 3.7+

### 설치 방법

```bash
# 저장소 클론
git clone https://github.com/jeoninch요즘/prompt-optimizer.git
cd prompt-optimizer

# 의존성 설치
pip install -r requirements.txt