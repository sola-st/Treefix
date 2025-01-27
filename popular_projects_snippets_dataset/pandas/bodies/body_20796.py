# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if tolerance is not None:
    tolerance = self._convert_tolerance(tolerance, target)

if method in ["pad", "backfill"]:
    indexer = self._get_fill_indexer(target, method, limit, tolerance)
elif method == "nearest":
    indexer = self._get_nearest_indexer(target, limit, tolerance)
else:
    if target._is_multi and self._is_multi:
        engine = self._engine
        # error: Item "IndexEngine" of "Union[IndexEngine, ExtensionEngine]"
        # has no attribute "_extract_level_codes"
        tgt_values = engine._extract_level_codes(  # type: ignore[union-attr]
            target
        )
    else:
        tgt_values = target._get_engine_target()

    indexer = self._engine.get_indexer(tgt_values)

exit(ensure_platform_int(indexer))
