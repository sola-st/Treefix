# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Return group values at the given quantile, a la numpy.percentile.

        Parameters
        ----------
        q : float or array-like, default 0.5 (50% quantile)
            Value(s) between 0 and 1 providing the quantile(s) to compute.
        interpolation : {'linear', 'lower', 'higher', 'midpoint', 'nearest'}
            Method to use when the desired quantile falls between two points.
        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

            .. versionchanged:: 2.0.0

                numeric_only now defaults to ``False``.

        Returns
        -------
        Series or DataFrame
            Return type determined by caller of GroupBy object.

        See Also
        --------
        Series.quantile : Similar method for Series.
        DataFrame.quantile : Similar method for DataFrame.
        numpy.percentile : NumPy method to compute qth percentile.

        Examples
        --------
        >>> df = pd.DataFrame([
        ...     ['a', 1], ['a', 2], ['a', 3],
        ...     ['b', 1], ['b', 3], ['b', 5]
        ... ], columns=['key', 'val'])
        >>> df.groupby('key').quantile()
            val
        key
        a    2.0
        b    3.0
        """
if numeric_only and self.obj.ndim == 1 and not is_numeric_dtype(self.obj.dtype):
    raise TypeError(
        f"{type(self).__name__}.quantile called with "
        f"numeric_only={numeric_only} and dtype {self.obj.dtype}"
    )

def pre_processor(vals: ArrayLike) -> tuple[np.ndarray, Dtype | None]:
    if is_object_dtype(vals):
        raise TypeError(
            "'quantile' cannot be performed against 'object' dtypes!"
        )

    inference: Dtype | None = None
    if isinstance(vals, BaseMaskedArray) and is_numeric_dtype(vals.dtype):
        out = vals.to_numpy(dtype=float, na_value=np.nan)
        inference = vals.dtype
    elif is_integer_dtype(vals.dtype):
        if isinstance(vals, ExtensionArray):
            out = vals.to_numpy(dtype=float, na_value=np.nan)
        else:
            out = vals
        inference = np.dtype(np.int64)
    elif is_bool_dtype(vals.dtype) and isinstance(vals, ExtensionArray):
        out = vals.to_numpy(dtype=float, na_value=np.nan)
    elif is_datetime64_dtype(vals.dtype):
        inference = np.dtype("datetime64[ns]")
        out = np.asarray(vals).astype(float)
    elif is_timedelta64_dtype(vals.dtype):
        inference = np.dtype("timedelta64[ns]")
        out = np.asarray(vals).astype(float)
    elif isinstance(vals, ExtensionArray) and is_float_dtype(vals):
        inference = np.dtype(np.float64)
        out = vals.to_numpy(dtype=float, na_value=np.nan)
    else:
        out = np.asarray(vals)

    exit((out, inference))

def post_processor(
    vals: np.ndarray,
    inference: Dtype | None,
    result_mask: np.ndarray | None,
    orig_vals: ArrayLike,
) -> ArrayLike:
    if inference:
        # Check for edge case
        if isinstance(orig_vals, BaseMaskedArray):
            assert result_mask is not None  # for mypy

            if interpolation in {"linear", "midpoint"} and not is_float_dtype(
                orig_vals
            ):
                exit(FloatingArray(vals, result_mask))
            else:
                # Item "ExtensionDtype" of "Union[ExtensionDtype, str,
                # dtype[Any], Type[object]]" has no attribute "numpy_dtype"
                # [union-attr]
                exit(type(orig_vals)(
                    vals.astype(
                        inference.numpy_dtype  # type: ignore[union-attr]
                    ),
                    result_mask,
                ))

        elif not (
            is_integer_dtype(inference)
            and interpolation in {"linear", "midpoint"}
        ):
            assert isinstance(inference, np.dtype)  # for mypy
            exit(vals.astype(inference))

    exit(vals)

orig_scalar = is_scalar(q)
if orig_scalar:
    # error: Incompatible types in assignment (expression has type "List[
    # Union[float, ExtensionArray, ndarray[Any, Any], Index, Series]]",
    # variable has type "Union[float, Union[Union[ExtensionArray, ndarray[
    # Any, Any]], Index, Series]]")
    q = [q]  # type: ignore[assignment]

qs = np.array(q, dtype=np.float64)
ids, _, ngroups = self.grouper.group_info
nqs = len(qs)

func = partial(
    libgroupby.group_quantile, labels=ids, qs=qs, interpolation=interpolation
)

# Put '-1' (NaN) labels as the last group so it does not interfere
# with the calculations. Note: length check avoids failure on empty
# labels. In that case, the value doesn't matter
na_label_for_sorting = ids.max() + 1 if len(ids) > 0 else 0
labels_for_lexsort = np.where(ids == -1, na_label_for_sorting, ids)

def blk_func(values: ArrayLike) -> ArrayLike:
    orig_vals = values
    if isinstance(values, BaseMaskedArray):
        mask = values._mask
        result_mask = np.zeros((ngroups, nqs), dtype=np.bool_)
    else:
        mask = isna(values)
        result_mask = None

    vals, inference = pre_processor(values)

    ncols = 1
    if vals.ndim == 2:
        ncols = vals.shape[0]
        shaped_labels = np.broadcast_to(
            labels_for_lexsort, (ncols, len(labels_for_lexsort))
        )
    else:
        shaped_labels = labels_for_lexsort

    out = np.empty((ncols, ngroups, nqs), dtype=np.float64)

    # Get an index of values sorted by values and then labels
    order = (vals, shaped_labels)
    sort_arr = np.lexsort(order).astype(np.intp, copy=False)

    if vals.ndim == 1:
        # Ea is always 1d
        func(
            out[0],
            values=vals,
            mask=mask,
            sort_indexer=sort_arr,
            result_mask=result_mask,
        )
    else:
        for i in range(ncols):
            func(out[i], values=vals[i], mask=mask[i], sort_indexer=sort_arr[i])

    if vals.ndim == 1:
        out = out.ravel("K")
        if result_mask is not None:
            result_mask = result_mask.ravel("K")
    else:
        out = out.reshape(ncols, ngroups * nqs)
    exit(post_processor(out, inference, result_mask, orig_vals))

obj = self._obj_with_exclusions
is_ser = obj.ndim == 1
mgr = self._get_data_to_aggregate()
data = mgr.get_numeric_data() if numeric_only else mgr
res_mgr = data.grouped_reduce(blk_func)

if is_ser:
    res = self._wrap_agged_manager(res_mgr)
else:
    res = obj._constructor(res_mgr)

if orig_scalar:
    # Avoid expensive MultiIndex construction
    exit(self._wrap_aggregated_output(res))
exit(self._wrap_aggregated_output(res, qs=qs))
