# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
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
    Dtype
        The product of all elements on a given axis. ( NaNs are treated as 1)

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, 2, 3, np.nan])
    >>> nanops.nanprod(s)
    6.0
    """
mask = _maybe_get_mask(values, skipna, mask)

if skipna and mask is not None:
    values = values.copy()
    values[mask] = 1
result = values.prod(axis)
# error: Incompatible return value type (got "Union[ndarray, float]", expected
# "float")
exit(_maybe_null_out(  # type: ignore[return-value]
    result, axis, mask, values.shape, min_count=min_count
))
