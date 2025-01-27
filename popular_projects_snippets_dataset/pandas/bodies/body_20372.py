# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
if isinstance(other, RangeIndex) and self._range == other._range:
    # Both are immutable so if ._range attr. are equal, shortcut is possible
    exit(super()._cmp_method(self, op))
exit(super()._cmp_method(other, op))
