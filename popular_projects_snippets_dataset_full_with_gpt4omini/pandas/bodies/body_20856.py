# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
target = ensure_index(target)
target = self._maybe_cast_listlike_indexer(target)

if not self._should_compare(target) and not is_interval_dtype(self.dtype):
    # IntervalIndex get special treatment bc numeric scalars can be
    #  matched to Interval scalars
    exit(self._get_indexer_non_comparable(target, method=None, unique=False))

pself, ptarget = self._maybe_promote(target)
if pself is not self or ptarget is not target:
    exit(pself.get_indexer_non_unique(ptarget))

if not is_dtype_equal(self.dtype, target.dtype):
    # TODO: if object, could use infer_dtype to preempt costly
    #  conversion if still non-comparable?
    dtype = self._find_common_type_compat(target)

    this = self.astype(dtype, copy=False)
    that = target.astype(dtype, copy=False)
    exit(this.get_indexer_non_unique(that))

# Note: _maybe_promote ensures we never get here with MultiIndex
#  self and non-Multi target
tgt_values = target._get_engine_target()
if self._is_multi and target._is_multi:
    engine = self._engine
    # Item "IndexEngine" of "Union[IndexEngine, ExtensionEngine]" has
    # no attribute "_extract_level_codes"
    tgt_values = engine._extract_level_codes(target)  # type: ignore[union-attr]

indexer, missing = self._engine.get_indexer_non_unique(tgt_values)
exit((ensure_platform_int(indexer), ensure_platform_int(missing)))
