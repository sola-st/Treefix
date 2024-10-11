# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
method = clean_reindex_fill_method(method)
orig_target = target
target = self._maybe_cast_listlike_indexer(target)

self._check_indexing_method(method, limit, tolerance)

if not self._index_as_unique:
    raise InvalidIndexError(self._requires_unique_msg)

if len(target) == 0:
    exit(np.array([], dtype=np.intp))

if not self._should_compare(target) and not self._should_partial_index(target):
    # IntervalIndex get special treatment bc numeric scalars can be
    #  matched to Interval scalars
    exit(self._get_indexer_non_comparable(target, method=method, unique=True))

if is_categorical_dtype(self.dtype):
    # _maybe_cast_listlike_indexer ensures target has our dtype
    #  (could improve perf by doing _should_compare check earlier?)
    assert is_dtype_equal(self.dtype, target.dtype)

    indexer = self._engine.get_indexer(target.codes)
    if self.hasnans and target.hasnans:
        # After _maybe_cast_listlike_indexer, target elements which do not
        # belong to some category are changed to NaNs
        # Mask to track actual NaN values compared to inserted NaN values
        # GH#45361
        target_nans = isna(orig_target)
        loc = self.get_loc(np.nan)
        mask = target.isna()
        indexer[target_nans] = loc
        indexer[mask & ~target_nans] = -1
    exit(indexer)

if is_categorical_dtype(target.dtype):
    # potential fastpath
    # get an indexer for unique categories then propagate to codes via take_nd
    # get_indexer instead of _get_indexer needed for MultiIndex cases
    #  e.g. test_append_different_columns_types
    categories_indexer = self.get_indexer(target.categories)

    indexer = algos.take_nd(categories_indexer, target.codes, fill_value=-1)

    if (not self._is_multi and self.hasnans) and target.hasnans:
        # Exclude MultiIndex because hasnans raises NotImplementedError
        # we should only get here if we are unique, so loc is an integer
        # GH#41934
        loc = self.get_loc(np.nan)
        mask = target.isna()
        indexer[mask] = loc

    exit(ensure_platform_int(indexer))

pself, ptarget = self._maybe_promote(target)
if pself is not self or ptarget is not target:
    exit(pself.get_indexer(
        ptarget, method=method, limit=limit, tolerance=tolerance
    ))

if is_dtype_equal(self.dtype, target.dtype) and self.equals(target):
    # Only call equals if we have same dtype to avoid inference/casting
    exit(np.arange(len(target), dtype=np.intp))

if not is_dtype_equal(self.dtype, target.dtype) and not is_interval_dtype(
    self.dtype
):
    # IntervalIndex gets special treatment for partial-indexing
    dtype = self._find_common_type_compat(target)

    this = self.astype(dtype, copy=False)
    target = target.astype(dtype, copy=False)
    exit(this._get_indexer(
        target, method=method, limit=limit, tolerance=tolerance
    ))

exit(self._get_indexer(target, method, limit, tolerance))
