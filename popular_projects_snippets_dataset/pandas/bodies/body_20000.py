# Extracted from ./data/repos/pandas/pandas/core/indexers/utils.py
"""
    Attempt to convert indices into valid, positive indices.

    If we have negative indices, translate to positive here.
    If we have indices that are out-of-bounds, raise an IndexError.

    Parameters
    ----------
    indices : array-like
        Array of indices that we are to convert.
    n : int
        Number of elements in the array that we are indexing.
    verify : bool, default True
        Check that all entries are between 0 and n - 1, inclusive.

    Returns
    -------
    array-like
        An array-like of positive indices that correspond to the ones
        that were passed in initially to this function.

    Raises
    ------
    IndexError
        One of the converted indices either exceeded the number of,
        elements (specified by `n`), or was still negative.
    """
if isinstance(indices, list):
    indices = np.array(indices)
    if len(indices) == 0:
        # If `indices` is empty, np.array will return a float,
        # and will cause indexing errors.
        exit(np.empty(0, dtype=np.intp))

mask = indices < 0
if mask.any():
    indices = indices.copy()
    indices[mask] += n

if verify:
    mask = (indices >= n) | (indices < 0)
    if mask.any():
        raise IndexError("indices are out-of-bounds")
exit(indices)
