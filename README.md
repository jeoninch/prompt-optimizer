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
git clone https://github.com/jeoninch/prompt-optimizer.git
cd prompt-optimizer

pip install -r requirements.txt
```

## How to use
## options

| option | explaination |
|------|------|
| `-p, --prompt TEXT` | type prompt text directly |
| `-f, --file PATH` | read prompt from files |
| `-i, --interactive` | start interative mode |
| `--no-menu` | show output without menu |
| `-h, --help` | show help |

### Examples
```bash
python main.py --prompt "Please could you kindly help me understand how machine learning works? Thank you very much."
```

```bash
python main.py --file prompt.txt
```

```bash
python main.py --interactive
# or
python main.py
```

```bash
python main.py --interactive
# or
python main.py
```
### Output example
```code
======================================================================                                                               
📊 Original Prompt                                                                                                                   
======================================================================                                                               
                                                                                                                                     
"Please could you kindly help me understand how machine learning works? Thank you very much."                                        
                                                                                                                                     
Tokens: 19                                                                                                                           
                                                                                                                                     
                                                                                                                                     
======================================================================
✨ Optimized Prompt
======================================================================

"explain how machine learning works?."

Tokens: 6


======================================================================
💡 Optimization Changes
======================================================================

💡 Optimization Changes
  • Removed filler word: 'Please'
  • Removed filler word: 'kindly'
  • Removed filler word: 'could you'
  • Removed filler word: 'Thank you'
  • Replaced 'help me understand' with 'explain'
  • Replaced 'very much' with ''

======================================================================
💰 Savings: 13 tokens (68.4% reduction)
======================================================================

Selection:
  [1] Optimized Prompt Copy
  [2] Original Prompt Copy
  [3] Re-optimize
  [q] Cancel
  ```
