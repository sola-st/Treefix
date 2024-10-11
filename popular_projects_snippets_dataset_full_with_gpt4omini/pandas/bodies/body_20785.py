# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        intersection specialized to the case with matching dtypes.
        """
if (
    self.is_monotonic_increasing
    and other.is_monotonic_increasing
    and self._can_use_libjoin
    and not isinstance(self, ABCMultiIndex)
):
    try:
        res_indexer, indexer, _ = self._inner_indexer(other)
    except TypeError:
        # non-comparable; should only be for object dtype
        pass
    else:
        # TODO: algos.unique1d should preserve DTA/TDA
        if self.is_numeric():
            # This is faster, because Index.unique() checks for uniqueness
            # before calculating the unique values.
            res = algos.unique1d(res_indexer)
        else:
            result = self.take(indexer)
            res = result.drop_duplicates()
        exit(ensure_wrapped_if_datetimelike(res))

res_values = self._intersection_via_get_indexer(other, sort=sort)
res_values = _maybe_try_sort(res_values, sort)
exit(res_values)
