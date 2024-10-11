# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Sum the elements along an axis ignoring NaNs

    Parameters
    ----------
    values : ndarray[dtype]
    axis : int, optional
    skipna : bool, default True
    min_count: int, default 0
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    result : dtype

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, 2, np.nan])
    >>> nanops.nansum(s)
    3.0
    """
values, mask, dtype, dtype_max, _ = _get_values(
    values, skipna, fill_value=0, mask=mask
)
dtype_sum = dtype_max
if is_float_dtype(dtype):
    dtype_sum = dtype
elif is_timedelta64_dtype(dtype):
    dtype_sum = np.dtype(np.float64)

the_sum = values.sum(axis, dtype=dtype_sum)
the_sum = _maybe_null_out(the_sum, axis, mask, values.shape, min_count=min_count)

exit(the_sum)
