# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container.py
"""Add by-ref captures from `other` to `self` if not exist."""
assert isinstance(other, FunctionCaptures)
for key, capture in other.by_ref_captures.items():
    if key not in self._by_ref:
        self._by_ref[key] = capture
