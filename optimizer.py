import re
from typing import Tuple, List


class PromptOptimizer:
    """Rule-based prompt optimizer for token efficiency"""

    # Words to remove
    FILLER_WORDS = [
        r'\bplease\b',
        r'\bkindly\b',
        r'\bcould\s+you\b',
        r'\bwould\s+you\b',
        r'\bcan\s+you\b',
        r'\bwill\s+you\b',
        r'\bi\s+would\s+appreciate\b',
        r'\bif\s+you\s+don\'t\s+mind\b',
        r'\bif\s+possible\b',
        r'\bthank\s+you\b',
        r'\bthanks\b',
        r'\bthank\s+you\s+very\s+much\b',
    ]

    # Verbose expressions to simplify
    REPLACEMENTS = [
        (r'\bas\s+soon\s+as\s+possible\b', 'ASAP'),
        (r'\bcan\s+you\s+help\s+me\b', 'help'),
        (r'\bhelp\s+me\s+understand\b', 'explain'),
        (r'\bI\s+want\s+you\s+to\b', ''),
        (r'\bI\s+need\s+you\s+to\b', ''),
        (r'\bin\s+detail\b', ''),
        (r'\bvery\s+much\b', ''),
        (r'\bquite\s+a\s+bit\b', ''),
    ]

    # Intensifiers to remove or reduce
    INTENSIFIERS = [
        r'\bvery\b',
        r'\breally\b',
        r'\bso\b',
        r'\bjust\b',
        r'\babsolutely\b',
        r'\bdefinitely\b',
    ]

    def __init__(self):
        self.changes = []

    def estimate_tokens(self, text: str) -> int:
        """
        Estimate token count using simple heuristic.
        Rough approximation: 1 token ≈ 4 characters or 1 word
        """
        # Split by whitespace and punctuation
        words = re.findall(r'\b\w+\b', text)
        # Rough estimate: average ~1.3 tokens per word in English
        return max(1, int(len(words) * 1.3))

    def optimize(self, prompt: str) -> Tuple[str, List[str]]:
        """
        Optimize the prompt and return optimized text + list of changes.
        
        Returns:
            Tuple of (optimized_prompt, changes_list)
        """
        self.changes = []
        text = prompt.strip()
        original_text = text

        # Step 1: Remove filler words
        for pattern in self.FILLER_WORDS:
            if re.search(pattern, text, re.IGNORECASE):
                text = re.sub(pattern, '', text, flags=re.IGNORECASE)
                word = re.search(pattern, original_text, re.IGNORECASE)
                if word:
                    self.changes.append(f"Removed filler word: '{word.group()}'")

        # Step 2: Apply replacements
        for pattern, replacement in self.REPLACEMENTS:
            if re.search(pattern, text, re.IGNORECASE):
                new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
                if new_text != text:
                    match = re.search(pattern, text, re.IGNORECASE)
                    self.changes.append(
                        f"Replaced '{match.group()}' with '{replacement}'"
                    )
                    text = new_text

        # Step 3: Remove intensifiers
        for pattern in self.INTENSIFIERS:
            if re.search(pattern, text, re.IGNORECASE):
                text = re.sub(pattern, '', text, flags=re.IGNORECASE)
                self.changes.append(f"Removed intensifier: '{pattern.strip(chr(92))}'")

        # Step 4: Clean up multiple spaces
        text = re.sub(r'\s+', ' ', text)

        # Step 5: Clean up punctuation spacing
        text = re.sub(r'\s+([.,!?;:])', r'\1', text)
        text = re.sub(r'([.,!?;:])\s+', r'\1 ', text)

        # Step 6: Remove trailing/leading spaces
        text = text.strip()

        # Mark if we improved punctuation
        if text != original_text and original_text.strip() == text.strip():
            self.changes.append("Improved punctuation structure")

        return text, self.changes

    def compare(self, original: str, optimized: str) -> dict:
        """
        Compare original and optimized prompts.
        
        Returns:
            Dictionary with comparison stats
        """
        original_tokens = self.estimate_tokens(original)
        optimized_tokens = self.estimate_tokens(optimized)
        saved_tokens = original_tokens - optimized_tokens
        savings_percent = (
            (saved_tokens / original_tokens * 100) if original_tokens > 0 else 0
        )

        return {
            'original_tokens': original_tokens,
            'optimized_tokens': optimized_tokens,
            'saved_tokens': saved_tokens,
            'savings_percent': savings_percent,
        }
