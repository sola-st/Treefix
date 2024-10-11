# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check whether the provided array or dtype is of the int64 dtype.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array or dtype is of the int64 dtype.

    Notes
    -----
    Depending on system architecture, the return value of `is_int64_dtype(
    int)` will be True if the OS uses 64-bit integers and False if the OS
    uses 32-bit integers.

    Examples
    --------
    >>> is_int64_dtype(str)
    False
    >>> is_int64_dtype(np.int32)
    False
    >>> is_int64_dtype(np.int64)
    True
    >>> is_int64_dtype('int8')
    False
    >>> is_int64_dtype('Int8')
    False
    >>> is_int64_dtype(pd.Int64Dtype)
    True
    >>> is_int64_dtype(float)
    False
    >>> is_int64_dtype(np.uint64)  # unsigned
    False
    >>> is_int64_dtype(np.array(['a', 'b']))
    False
    >>> is_int64_dtype(np.array([1, 2], dtype=np.int64))
    True
    >>> is_int64_dtype(pd.Index([1, 2.]))  # float
    False
    >>> is_int64_dtype(np.array([1, 2], dtype=np.uint32))  # unsigned
    False
    """
exit(_is_dtype_type(arr_or_dtype, classes(np.int64)))
