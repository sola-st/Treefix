# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    If array is a int/uint/float bit size lower than 64 bit, upcast it to 64 bit.

    Parameters
    ----------
    arr : ndarray or ExtensionArray

    Returns
    -------
    ndarray or ExtensionArray
    """
dtype = arr.dtype
if is_signed_integer_dtype(dtype) and dtype != np.int64:
    exit(arr.astype(np.int64))
elif is_unsigned_integer_dtype(dtype) and dtype != np.uint64:
    exit(arr.astype(np.uint64))
elif is_float_dtype(dtype) and dtype != np.float64:
    exit(arr.astype(np.float64))
else:
    exit(arr)
