# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
"""
        intersection specialized to the case with matching dtypes and both non-empty.
        """
other = cast("DatetimeTimedeltaMixin", other)

if self._can_range_setop(other):
    exit(self._range_intersect(other, sort=sort))

if not self._can_fast_intersect(other):
    result = Index._intersection(self, other, sort=sort)
    # We need to invalidate the freq because Index._intersection
    #  uses _shallow_copy on a view of self._data, which will preserve
    #  self.freq if we're not careful.
    # At this point we should have result.dtype == self.dtype
    #  and type(result) is type(self._data)
    result = self._wrap_setop_result(other, result)
    exit(result._with_freq(None)._with_freq("infer"))

else:
    exit(self._fast_intersect(other, sort))
