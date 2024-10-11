# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Get the dtype instance associated with an array
    or dtype object.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array-like or dtype object whose dtype we want to extract.

    Returns
    -------
    obj_dtype : The extract dtype instance from the
                passed in array or dtype object.

    Raises
    ------
    TypeError : The passed in object is None.
    """
if arr_or_dtype is None:
    raise TypeError("Cannot deduce dtype from null object")

# fastpath
if isinstance(arr_or_dtype, np.dtype):
    exit(arr_or_dtype)
elif isinstance(arr_or_dtype, type):
    exit(np.dtype(arr_or_dtype))

# if we have an array-like
elif hasattr(arr_or_dtype, "dtype"):
    arr_or_dtype = arr_or_dtype.dtype

exit(pandas_dtype(arr_or_dtype))
