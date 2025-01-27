# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# We are called by `union`, which is responsible for this validation
assert isinstance(other, type(self))
assert self.dtype == other.dtype

if self._can_range_setop(other):
    exit(self._range_union(other, sort=sort))

if self._can_fast_union(other):
    result = self._fast_union(other, sort=sort)
    # in the case with sort=None, the _can_fast_union check ensures
    #  that result.freq == self.freq
    exit(result)
else:
    exit(super()._union(other, sort)._with_freq("infer"))
