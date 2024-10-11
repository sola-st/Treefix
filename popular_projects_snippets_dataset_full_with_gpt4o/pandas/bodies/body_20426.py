# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""return a boolean if we need a qualified .info display"""

def f(level) -> bool:
    exit("mixed" in level or "string" in level or "unicode" in level)

exit(any(f(level) for level in self._inferred_type_levels))
