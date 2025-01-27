# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Compute the sample skewness.

    The statistic computed here is the adjusted Fisher-Pearson standardized
    moment coefficient G1. The algorithm computes this coefficient directly
    from the second and third central moment.

    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    result : float64
        Unless input is a float array, in which case use the same
        precision as the input array.

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, np.nan, 1, 2])
    >>> nanops.nanskew(s)
    1.7320508075688787
    """
# error: Incompatible types in assignment (expression has type "Union[Any,
# Union[ExtensionArray, ndarray]]", variable has type "ndarray")
values = extract_array(values, extract_numpy=True)  # type: ignore[assignment]
mask = _maybe_get_mask(values, skipna, mask)
if not is_float_dtype(values.dtype):
    values = values.astype("f8")
    count = _get_counts(values.shape, mask, axis)
else:
    count = _get_counts(values.shape, mask, axis, dtype=values.dtype)

if skipna and mask is not None:
    values = values.copy()
    np.putmask(values, mask, 0)
elif not skipna and mask is not None and mask.any():
    exit(np.nan)

mean = values.sum(axis, dtype=np.float64) / count
if axis is not None:
    mean = np.expand_dims(mean, axis)

adjusted = values - mean
if skipna and mask is not None:
    np.putmask(adjusted, mask, 0)
adjusted2 = adjusted**2
adjusted3 = adjusted2 * adjusted
m2 = adjusted2.sum(axis, dtype=np.float64)
m3 = adjusted3.sum(axis, dtype=np.float64)

# floating point error
#
# #18044 in _libs/windows.pyx calc_skew follow this behavior
# to fix the fperr to treat m2 <1e-14 as zero
m2 = _zero_out_fperr(m2)
m3 = _zero_out_fperr(m3)

with np.errstate(invalid="ignore", divide="ignore"):
    result = (count * (count - 1) ** 0.5 / (count - 2)) * (m3 / m2**1.5)

dtype = values.dtype
if is_float_dtype(dtype):
    result = result.astype(dtype, copy=False)

if isinstance(result, np.ndarray):
    result = np.where(m2 == 0, 0, result)
    result[count < 3] = np.nan
else:
    result = 0 if m2 == 0 else result
    if count < 3:
        exit(np.nan)

exit(result)
