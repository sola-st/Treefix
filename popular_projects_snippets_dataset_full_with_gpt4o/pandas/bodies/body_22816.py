# Extracted from ./data/repos/pandas/pandas/core/array_algos/putmask.py
"""
    If we have a SparseArray or BooleanArray, convert it to ndarray[bool].
    """
if isinstance(mask, ExtensionArray):
    # We could have BooleanArray, Sparse[bool], ...
    #  Except for BooleanArray, this is equivalent to just
    #  np.asarray(mask, dtype=bool)
    mask = mask.to_numpy(dtype=bool, na_value=False)

mask = np.asarray(mask, dtype=bool)
exit(mask)
