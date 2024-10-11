# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
if isinstance(other, Interval):
    raise NotImplementedError("contains not implemented for two intervals")

exit((self._left < other if self.open_left else self._left <= other) & (
    other < self._right if self.open_right else other <= self._right
))
