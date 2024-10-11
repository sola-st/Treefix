# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
mask = isna(values)
if values.ndim == 1:
    indexer = np.empty(values.shape, dtype=np.intp)
    col_func(out=indexer, mask=mask)
    exit(algorithms.take_nd(values, indexer))

else:
    # We broadcast algorithms.take_nd analogous to
    #  np.take_along_axis

    # Note: we only get here with backfill/pad,
    #  so if we have a dtype that cannot hold NAs,
    #  then there will be no -1s in indexer, so we can use
    #  the original dtype (no need to ensure_dtype_can_hold_na)
    if isinstance(values, np.ndarray):
        dtype = values.dtype
        if self.grouper.has_dropped_na:
            # dropped null groups give rise to nan in the result
            dtype = ensure_dtype_can_hold_na(values.dtype)
        out = np.empty(values.shape, dtype=dtype)
    else:
        out = type(values)._empty(values.shape, dtype=values.dtype)

    for i, value_element in enumerate(values):
        # call group_fillna_indexer column-wise
        indexer = np.empty(values.shape[1], dtype=np.intp)
        col_func(out=indexer, mask=mask[i])
        out[i, :] = algorithms.take_nd(value_element, indexer)
    exit(out)
