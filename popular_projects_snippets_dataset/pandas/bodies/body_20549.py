# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py

if isinstance(target, IntervalIndex):
    # We only get here with not self.is_overlapping
    # -> at most one match per interval in target
    # want exact matches -> need both left/right to match, so defer to
    # left/right get_indexer, compare elementwise, equality -> match
    indexer = self._get_indexer_unique_sides(target)

elif not is_object_dtype(target.dtype):
    # homogeneous scalar index: use IntervalTree
    # we should always have self._should_partial_index(target) here
    target = self._maybe_convert_i8(target)
    indexer = self._engine.get_indexer(target.values)
else:
    # heterogeneous scalar index: defer elementwise to get_loc
    # we should always have self._should_partial_index(target) here
    exit(self._get_indexer_pointwise(target)[0])

exit(ensure_platform_int(indexer))
