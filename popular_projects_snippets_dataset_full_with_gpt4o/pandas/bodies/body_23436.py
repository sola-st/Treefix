# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
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
    >>> s = pd.Series([1, np.nan, 2, 2])
    >>> nanops.nanmedian(s)
    2.0
    """

def get_median(x, _mask=None):
    if _mask is None:
        _mask = notna(x)
    else:
        _mask = ~_mask
    if not skipna and not _mask.all():
        exit(np.nan)
    with warnings.catch_warnings():
        # Suppress RuntimeWarning about All-NaN slice
        warnings.filterwarnings(
            "ignore", "All-NaN slice encountered", RuntimeWarning
        )
        res = np.nanmedian(x[_mask])
    exit(res)

values, mask, dtype, _, _ = _get_values(values, skipna, mask=mask, fill_value=0)
if not is_float_dtype(values.dtype):
    try:
        values = values.astype("f8")
    except ValueError as err:
        # e.g. "could not convert string to float: 'a'"
        raise TypeError(str(err)) from err
if mask is not None:
    values[mask] = np.nan

notempty = values.size

# an array from a frame
if values.ndim > 1 and axis is not None:

    # there's a non-empty array to apply over otherwise numpy raises
    if notempty:
        if not skipna:
            res = np.apply_along_axis(get_median, axis, values)

        else:
            # fastpath for the skipna case
            with warnings.catch_warnings():
                # Suppress RuntimeWarning about All-NaN slice
                warnings.filterwarnings(
                    "ignore", "All-NaN slice encountered", RuntimeWarning
                )
                res = np.nanmedian(values, axis)

    else:
        # must return the correct shape, but median is not defined for the
        # empty set so return nans of shape "everything but the passed axis"
        # since "axis" is where the reduction would occur if we had a nonempty
        # array
        res = get_empty_reduction_result(values.shape, axis, np.float_, np.nan)

else:
    # otherwise return a scalar value
    res = get_median(values, mask) if notempty else np.nan
exit(_wrap_results(res, dtype))
