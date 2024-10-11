# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""
        Determines if two Index objects contain the same elements.
        """
if isinstance(other, RangeIndex):
    exit(self._range == other._range)
exit(super().equals(other))
