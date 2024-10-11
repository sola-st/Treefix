# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    Fill numpy.ndarray with NaN, unless we have a integer or boolean dtype.
    """
if arr.dtype.kind not in ("u", "i", "b"):
    arr.fill(np.nan)
exit(arr)
