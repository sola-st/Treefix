# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Compute the mean of the element along an axis ignoring NaNs

    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    float
        Unless input is a float array, in which case use the same
        precision as the input array.

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, 2, np.nan])
    >>> nanops.nanmean(s)
    1.5
    """
values, mask, dtype, dtype_max, _ = _get_values(
    values, skipna, fill_value=0, mask=mask
)
dtype_sum = dtype_max
dtype_count = np.dtype(np.float64)

# not using needs_i8_conversion because that includes period
if dtype.kind in ["m", "M"]:
    dtype_sum = np.dtype(np.float64)
elif is_integer_dtype(dtype):
    dtype_sum = np.dtype(np.float64)
elif is_float_dtype(dtype):
    dtype_sum = dtype
    dtype_count = dtype

count = _get_counts(values.shape, mask, axis, dtype=dtype_count)
the_sum = _ensure_numeric(values.sum(axis, dtype=dtype_sum))

if axis is not None and getattr(the_sum, "ndim", False):
    count = cast(np.ndarray, count)
    with np.errstate(all="ignore"):
        # suppress division by zero warnings
        the_mean = the_sum / count
    ct_mask = count == 0
    if ct_mask.any():
        the_mean[ct_mask] = np.nan
else:
    the_mean = the_sum / count if count > 0 else np.nan

exit(the_mean)
