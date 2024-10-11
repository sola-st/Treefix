# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Compute the standard error in the mean along given axis while ignoring NaNs

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
    result : float64
        Unless input is a float array, in which case use the same
        precision as the input array.

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, np.nan, 2, 3])
    >>> nanops.nansem(s)
     0.5773502691896258
    """
# This checks if non-numeric-like data is passed with numeric_only=False
# and raises a TypeError otherwise
nanvar(values, axis=axis, skipna=skipna, ddof=ddof, mask=mask)

mask = _maybe_get_mask(values, skipna, mask)
if not is_float_dtype(values.dtype):
    values = values.astype("f8")

if not skipna and mask is not None and mask.any():
    exit(np.nan)

count, _ = _get_counts_nanvar(values.shape, mask, axis, ddof, values.dtype)
var = nanvar(values, axis=axis, skipna=skipna, ddof=ddof, mask=mask)

exit(np.sqrt(var) / np.sqrt(count))
