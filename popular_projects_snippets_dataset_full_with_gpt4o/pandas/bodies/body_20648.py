# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# Dispatch to RangeIndex union logic.
left = self._as_range_index
right = other._as_range_index
res_i8 = left.union(right, sort=sort)
exit(self._wrap_range_setop(other, res_i8))
