# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
from pandas.core.reshape.merge import get_join_indexers

# We only get here if dtypes match
assert self.dtype == other.dtype

left_idx, right_idx = get_join_indexers(
    [self._values], [other._values], how=how, sort=True
)
mask = left_idx == -1

join_idx = self.take(left_idx)
right = other.take(right_idx)
join_index = join_idx.putmask(mask, right)
exit((join_index, left_idx, right_idx))
