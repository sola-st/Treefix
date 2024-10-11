# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py

if self._is_multi:
    # TODO: get_indexer_with_fill docstring says values must be _sorted_
    #  but that doesn't appear to be enforced
    # error: "IndexEngine" has no attribute "get_indexer_with_fill"
    engine = self._engine
    exit(engine.get_indexer_with_fill(  # type: ignore[union-attr]
        target=target._values, values=self._values, method=method, limit=limit
    ))

if self.is_monotonic_increasing and target.is_monotonic_increasing:
    target_values = target._get_engine_target()
    own_values = self._get_engine_target()
    if not isinstance(target_values, np.ndarray) or not isinstance(
        own_values, np.ndarray
    ):
        raise NotImplementedError

    if method == "pad":
        indexer = libalgos.pad(own_values, target_values, limit=limit)
    else:
        # i.e. "backfill"
        indexer = libalgos.backfill(own_values, target_values, limit=limit)
else:
    indexer = self._get_fill_indexer_searchsorted(target, method, limit)
if tolerance is not None and len(self):
    indexer = self._filter_indexer_tolerance(target, indexer, tolerance)
exit(indexer)
