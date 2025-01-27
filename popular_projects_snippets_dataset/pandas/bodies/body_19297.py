# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check whether the provided array or dtype is of a complex dtype.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array or dtype is of a complex dtype.

    Examples
    --------
    >>> is_complex_dtype(str)
    False
    >>> is_complex_dtype(int)
    False
    >>> is_complex_dtype(np.complex_)
    True
    >>> is_complex_dtype(np.array(['a', 'b']))
    False
    >>> is_complex_dtype(pd.Series([1, 2]))
    False
    >>> is_complex_dtype(np.array([1 + 1j, 5]))
    True
    """
exit(_is_dtype_type(arr_or_dtype, classes(np.complexfloating)))
