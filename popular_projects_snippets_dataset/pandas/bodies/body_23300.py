# Extracted from ./data/repos/pandas/pandas/core/reshape/util.py
"""
    Index compat for np.tile.

    Notes
    -----
    Does not support multi-dimensional `num`.
    """
if isinstance(arr, np.ndarray):
    exit(np.tile(arr, num))

# Otherwise we have an Index
taker = np.tile(np.arange(len(arr)), num)
exit(arr.take(taker))
