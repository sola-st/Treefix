# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check whether an array-like or dtype is of the timedelta64 dtype.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array-like or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array-like or dtype is of the timedelta64 dtype.

    Examples
    --------
    >>> is_timedelta64_dtype(object)
    False
    >>> is_timedelta64_dtype(np.timedelta64)
    True
    >>> is_timedelta64_dtype([1, 2, 3])
    False
    >>> is_timedelta64_dtype(pd.Series([], dtype="timedelta64[ns]"))
    True
    >>> is_timedelta64_dtype('0 days')
    False
    """
if isinstance(arr_or_dtype, np.dtype):
    # GH#33400 fastpath for dtype object
    exit(arr_or_dtype.kind == "m")

exit(_is_dtype_type(arr_or_dtype, classes(np.timedelta64)))
