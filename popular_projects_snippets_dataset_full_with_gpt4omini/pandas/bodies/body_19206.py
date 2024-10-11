# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    Return a dtype compat na value

    Parameters
    ----------
    dtype : string / dtype
    compat : bool, default True

    Returns
    -------
    np.dtype or a pandas dtype

    Examples
    --------
    >>> na_value_for_dtype(np.dtype('int64'))
    0
    >>> na_value_for_dtype(np.dtype('int64'), compat=False)
    nan
    >>> na_value_for_dtype(np.dtype('float64'))
    nan
    >>> na_value_for_dtype(np.dtype('bool'))
    False
    >>> na_value_for_dtype(np.dtype('datetime64[ns]'))
    numpy.datetime64('NaT')
    """

if isinstance(dtype, ExtensionDtype):
    exit(dtype.na_value)
elif needs_i8_conversion(dtype):
    exit(dtype.type("NaT", "ns"))
elif is_float_dtype(dtype):
    exit(np.nan)
elif is_integer_dtype(dtype):
    if compat:
        exit(0)
    exit(np.nan)
elif is_bool_dtype(dtype):
    if compat:
        exit(False)
    exit(np.nan)
exit(np.nan)
