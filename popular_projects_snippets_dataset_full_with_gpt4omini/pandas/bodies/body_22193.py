# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Shared function for `pad` and `backfill` to call Cython method.

        Parameters
        ----------
        direction : {'ffill', 'bfill'}
            Direction passed to underlying Cython function. `bfill` will cause
            values to be filled backwards. `ffill` and any other values will
            default to a forward fill
        limit : int, default None
            Maximum number of consecutive values to fill. If `None`, this
            method will convert to -1 prior to passing to Cython

        Returns
        -------
        `Series` or `DataFrame` with filled values

        See Also
        --------
        pad : Returns Series with minimum number of char in object.
        backfill : Backward fill the missing values in the dataset.
        """
# Need int value for Cython
if limit is None:
    limit = -1

ids, _, _ = self.grouper.group_info
sorted_labels = np.argsort(ids, kind="mergesort").astype(np.intp, copy=False)
if direction == "bfill":
    sorted_labels = sorted_labels[::-1]

col_func = partial(
    libgroupby.group_fillna_indexer,
    labels=ids,
    sorted_labels=sorted_labels,
    direction=direction,
    limit=limit,
    dropna=self.dropna,
)

def blk_func(values: ArrayLike) -> ArrayLike:
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

obj = self._obj_with_exclusions
if self.axis == 1:
    obj = obj.T
mgr = obj._mgr
res_mgr = mgr.apply(blk_func)

new_obj = obj._constructor(res_mgr)
if isinstance(new_obj, Series):
    new_obj.name = obj.name

exit(self._wrap_transformed_output(new_obj))
