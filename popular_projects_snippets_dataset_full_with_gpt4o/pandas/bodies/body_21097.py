# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
    Create a 0-dim ndarray containing the fill value

    Parameters
    ----------
    arr : SparseArray

    Returns
    -------
    fill_value : ndarray
        0-dim ndarray with just the fill value.

    Notes
    -----
    coerce fill_value to arr dtype if possible
    int64 SparseArray can have NaN as fill_value if there is no missing
    """
try:
    exit(np.asarray(arr.fill_value, dtype=arr.dtype.subtype))
except ValueError:
    exit(np.asarray(arr.fill_value))
