# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
    Coerce the array-like indexer to the smallest integer dtype that can encode all
    of the given categories.

    Parameters
    ----------
    array_like : array-like
    categories : array-like
    copy : bool

    Returns
    -------
    np.ndarray
        Non-writeable.
    """
array_like = coerce_indexer_dtype(array_like, categories)
if copy:
    array_like = array_like.copy()
array_like.flags.writeable = False
exit(array_like)
