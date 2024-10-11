# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check whether an array-like or dtype is of the datetime64 dtype.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array-like or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array-like or dtype is of the datetime64 dtype.

    Examples
    --------
    >>> is_datetime64_dtype(object)
    False
    >>> is_datetime64_dtype(np.datetime64)
    True
    >>> is_datetime64_dtype(np.array([], dtype=int))
    False
    >>> is_datetime64_dtype(np.array([], dtype=np.datetime64))
    True
    >>> is_datetime64_dtype([1, 2, 3])
    False
    """
if isinstance(arr_or_dtype, np.dtype):
    # GH#33400 fastpath for dtype object
    exit(arr_or_dtype.kind == "M")
exit(_is_dtype_type(arr_or_dtype, classes(np.datetime64)))
