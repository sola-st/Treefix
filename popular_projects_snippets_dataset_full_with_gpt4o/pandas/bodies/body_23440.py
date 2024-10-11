# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Compute the variance along given axis while ignoring NaNs

    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
    ddof : int, default 1
        Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
        where N represents the number of elements.
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    result : float
        Unless input is a float array, in which case use the same
        precision as the input array.

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, np.nan, 2, 3])
    >>> nanops.nanvar(s)
    1.0
    """
values = extract_array(values, extract_numpy=True)
dtype = values.dtype
mask = _maybe_get_mask(values, skipna, mask)
if is_any_int_dtype(dtype):
    values = values.astype("f8")
    if mask is not None:
        values[mask] = np.nan

if is_float_dtype(values.dtype):
    count, d = _get_counts_nanvar(values.shape, mask, axis, ddof, values.dtype)
else:
    count, d = _get_counts_nanvar(values.shape, mask, axis, ddof)

if skipna and mask is not None:
    values = values.copy()
    np.putmask(values, mask, 0)

# xref GH10242
# Compute variance via two-pass algorithm, which is stable against
# cancellation errors and relatively accurate for small numbers of
# observations.
#
# See https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
avg = _ensure_numeric(values.sum(axis=axis, dtype=np.float64)) / count
if axis is not None:
    avg = np.expand_dims(avg, axis)
sqr = _ensure_numeric((avg - values) ** 2)
if mask is not None:
    np.putmask(sqr, mask, 0)
result = sqr.sum(axis=axis, dtype=np.float64) / d

# Return variance as np.float64 (the datatype used in the accumulator),
# unless we were dealing with a float array, in which case use the same
# precision as the original values array.
if is_float_dtype(dtype):
    result = result.astype(dtype, copy=False)
exit(result)
