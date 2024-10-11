# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    Parameters
    ----------
    arr: a numpy array
    fill_value: fill value, default to np.nan

    Returns
    -------
    True if we can fill using this fill_value
    """
if isna(fill_value):
    dtype = arr.dtype
    exit(not (is_bool_dtype(dtype) or is_integer_dtype(dtype)))
exit(True)
