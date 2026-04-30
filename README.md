# Prompt Optimizer

A CLI tool for optimizing AI prompts. 
Reduce token usage and improve efficiency before running prompts on ChatGPT or Claude.

## Features

- Token Count Analysis – Compare token usage between the original and optimized prompt
- Automatic Optimization – Rule-based prompt optimization engine
- Before/After Comparison – Visually review improvements
- File Input Support – Load prompts directly from files
- Interactive Mode – Optimize prompts multiple times in one session

## How it optimizes

- Removes unnecessary polite phrases (please, kindly, could you, etc.)
- Removes gratitude phrases (thank you, thanks, etc.)
- Cleans up filler or exaggerated words (very, really, just, etc.)
- Replaces verbose synonyms with simpler wording
- Improves structure, formatting, and spacing

## Installation

### Requirements
- Python 3.7+

### How to install

```bash
# 저장소 클론
git clone https://github.com/jeoninch요즘/prompt-optimizer.git
cd prompt-optimizer

# 의존성 설치
pip install -r requirements.txt
