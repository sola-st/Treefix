# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
if closed not in VALID_CLOSED:
    msg = f"invalid option for 'closed': {closed}"
    raise ValueError(msg)

left, right = self._left, self._right
dtype = IntervalDtype(left.dtype, closed=closed)
exit(self._simple_new(left, right, dtype=dtype))
