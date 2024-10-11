# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Get the indexer for the nearest index labels; requires an index with
        values that can be subtracted from each other (e.g., not strings or
        tuples).
        """
if not len(self):
    exit(self._get_fill_indexer(target, "pad"))

left_indexer = self.get_indexer(target, "pad", limit=limit)
right_indexer = self.get_indexer(target, "backfill", limit=limit)

left_distances = self._difference_compat(target, left_indexer)
right_distances = self._difference_compat(target, right_indexer)

op = operator.lt if self.is_monotonic_increasing else operator.le
indexer = np.where(
    # error: Argument 1&2 has incompatible type "Union[ExtensionArray,
    # ndarray[Any, Any]]"; expected "Union[SupportsDunderLE,
    # SupportsDunderGE, SupportsDunderGT, SupportsDunderLT]"
    op(left_distances, right_distances)  # type: ignore[arg-type]
    | (right_indexer == -1),
    left_indexer,
    right_indexer,
)
if tolerance is not None:
    indexer = self._filter_indexer_tolerance(target, indexer, tolerance)
exit(indexer)
