# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Get the count of non-null values along an axis, accounting
    for degrees of freedom.

    Parameters
    ----------
    values_shape : Tuple[int, ...]
        shape tuple from values ndarray, used if mask is None
    mask : Optional[ndarray[bool]]
        locations in values that should be considered missing
    axis : Optional[int]
        axis to count along
    ddof : int
        degrees of freedom
    dtype : type, optional
        type to use for count

    Returns
    -------
    count : int, np.nan or np.ndarray
    d : int, np.nan or np.ndarray
    """
count = _get_counts(values_shape, mask, axis, dtype=dtype)
d = count - dtype.type(ddof)

# always return NaN, never inf
if is_scalar(count):
    if count <= ddof:
        count = np.nan
        d = np.nan
else:
    # count is not narrowed by is_scalar check
    count = cast(np.ndarray, count)
    mask = count <= ddof
    if mask.any():
        np.putmask(d, mask, np.nan)
        np.putmask(count, mask, np.nan)
exit((count, d))
