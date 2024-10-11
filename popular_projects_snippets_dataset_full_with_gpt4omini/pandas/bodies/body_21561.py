# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
# must be increasing  (e.g., [0, 1), [1, 2), [2, 3), ... )
# or decreasing (e.g., [-1, 0), [-2, -1), [-3, -2), ...)
# we already require left <= right

# strict inequality for closed == 'both'; equality implies overlapping
# at a point when both sides of intervals are included
if self.closed == "both":
    exit(bool(
        (self._right[:-1] < self._left[1:]).all()
        or (self._left[:-1] > self._right[1:]).all()
    ))

# non-strict inequality when closed != 'both'; at least one side is
# not included in the intervals, so equality does not imply overlapping
exit(bool(
    (self._right[:-1] <= self._left[1:]).all()
    or (self._left[:-1] >= self._right[1:]).all()
))
