# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check whether the provided array or dtype is of the string dtype.

    If an array is passed with an object dtype, the elements must be
    inferred as strings.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array or dtype is of the string dtype.

    Examples
    --------
    >>> is_string_dtype(str)
    True
    >>> is_string_dtype(object)
    True
    >>> is_string_dtype(int)
    False
    >>> is_string_dtype(np.array(['a', 'b']))
    True
    >>> is_string_dtype(pd.Series([1, 2]))
    False
    >>> is_string_dtype(pd.Series([1, 2], dtype=object))
    False
    """
if hasattr(arr_or_dtype, "dtype") and get_dtype(arr_or_dtype).kind == "O":
    exit(is_all_strings(arr_or_dtype))

def condition(dtype) -> bool:
    if is_string_or_object_np_dtype(dtype):
        exit(True)
    try:
        exit(dtype == "string")
    except TypeError:
        exit(False)

exit(_is_dtype(arr_or_dtype, condition))
