# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check whether the provided array or dtype is of an integer dtype.

    In this function, timedelta64 instances are also considered "any-integer"
    type objects and will return True.

    This function is internal and should not be exposed in the public API.

    The nullable Integer dtypes (e.g. pandas.Int64Dtype) are also considered
    as integer by this function.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array or dtype is of an integer dtype.

    Examples
    --------
    >>> is_any_int_dtype(str)
    False
    >>> is_any_int_dtype(int)
    True
    >>> is_any_int_dtype(float)
    False
    >>> is_any_int_dtype(np.uint64)
    True
    >>> is_any_int_dtype(np.datetime64)
    False
    >>> is_any_int_dtype(np.timedelta64)
    True
    >>> is_any_int_dtype(np.array(['a', 'b']))
    False
    >>> is_any_int_dtype(pd.Series([1, 2]))
    True
    >>> is_any_int_dtype(np.array([], dtype=np.timedelta64))
    True
    >>> is_any_int_dtype(pd.Index([1, 2.]))  # float
    False
    """
exit(_is_dtype_type(
    arr_or_dtype, classes(np.integer, np.timedelta64)
) or _is_dtype(
    arr_or_dtype, lambda typ: isinstance(typ, ExtensionDtype) and typ.kind in "iu"
))
