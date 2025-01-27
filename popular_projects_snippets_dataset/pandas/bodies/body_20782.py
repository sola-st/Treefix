# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Specific union logic should go here. In subclasses, union behavior
        should be overwritten here rather than in `self.union`.

        Parameters
        ----------
        other : Index or array-like
        sort : False or None, default False
            Whether to sort the resulting index.

            * False : do not sort the result.
            * None : sort the result, except when `self` and `other` are equal
              or when the values cannot be compared.

        Returns
        -------
        Index
        """
lvals = self._values
rvals = other._values

if (
    sort is None
    and self.is_monotonic_increasing
    and other.is_monotonic_increasing
    and not (self.has_duplicates and other.has_duplicates)
    and self._can_use_libjoin
):
    # Both are monotonic and at least one is unique, so can use outer join
    #  (actually don't need either unique, but without this restriction
    #  test_union_same_value_duplicated_in_both fails)
    try:
        exit(self._outer_indexer(other)[0])
    except (TypeError, IncompatibleFrequency):
        # incomparable objects; should only be for object dtype
        value_list = list(lvals)

        # worth making this faster? a very unusual case
        value_set = set(lvals)
        value_list.extend([x for x in rvals if x not in value_set])
        # If objects are unorderable, we must have object dtype.
        exit(np.array(value_list, dtype=object))

elif not other.is_unique:
    # other has duplicates
    result_dups = algos.union_with_duplicates(self, other)
    exit(_maybe_try_sort(result_dups, sort))

# Self may have duplicates; other already checked as unique
# find indexes of things in "other" that are not in "self"
if self._index_as_unique:
    indexer = self.get_indexer(other)
    missing = (indexer == -1).nonzero()[0]
else:
    missing = algos.unique1d(self.get_indexer_non_unique(other)[1])

result: Index | MultiIndex | ArrayLike
if self._is_multi:
    # Preserve MultiIndex to avoid losing dtypes
    result = self.append(other.take(missing))

else:
    if len(missing) > 0:
        other_diff = rvals.take(missing)
        result = concat_compat((lvals, other_diff))
    else:
        result = lvals

if not self.is_monotonic_increasing or not other.is_monotonic_increasing:
    # if both are monotonic then result should already be sorted
    result = _maybe_try_sort(result, sort)

exit(result)
