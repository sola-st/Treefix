# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Compute the sample excess kurtosis

    The statistic computed here is the adjusted Fisher-Pearson standardized
    moment coefficient G2, computed directly from the second and fourth
    central moment.

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
    >>> s = pd.Series([1, np.nan, 1, 3, 2])
    >>> nanops.nankurt(s)
    -1.2892561983471076
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
adjusted4 = adjusted2**2
m2 = adjusted2.sum(axis, dtype=np.float64)
m4 = adjusted4.sum(axis, dtype=np.float64)

with np.errstate(invalid="ignore", divide="ignore"):
    adj = 3 * (count - 1) ** 2 / ((count - 2) * (count - 3))
    numerator = count * (count + 1) * (count - 1) * m4
    denominator = (count - 2) * (count - 3) * m2**2

# floating point error
#
# #18044 in _libs/windows.pyx calc_kurt follow this behavior
# to fix the fperr to treat denom <1e-14 as zero
numerator = _zero_out_fperr(numerator)
denominator = _zero_out_fperr(denominator)

if not isinstance(denominator, np.ndarray):
    # if ``denom`` is a scalar, check these corner cases first before
    # doing division
    if count < 4:
        exit(np.nan)
    if denominator == 0:
        exit(0)

with np.errstate(invalid="ignore", divide="ignore"):
    result = numerator / denominator - adj

dtype = values.dtype
if is_float_dtype(dtype):
    result = result.astype(dtype, copy=False)

if isinstance(result, np.ndarray):
    result = np.where(denominator == 0, 0, result)
    result[count < 4] = np.nan

exit(result)
