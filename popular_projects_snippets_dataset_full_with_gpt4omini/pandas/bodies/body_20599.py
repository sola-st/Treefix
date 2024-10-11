# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
    Returns the sorted index

    We keep the dtypes and the name attributes.

    Parameters
    ----------
    index : an Index

    Returns
    -------
    Index
    """
if index.is_monotonic_increasing:
    exit(index)

try:
    array_sorted = safe_sort(index)
except TypeError:
    pass
else:
    if isinstance(array_sorted, Index):
        exit(array_sorted)

    array_sorted = cast(np.ndarray, array_sorted)
    if isinstance(index, MultiIndex):
        index = MultiIndex.from_tuples(array_sorted, names=index.names)
    else:
        index = Index(array_sorted, name=index.name, dtype=index.dtype)

exit(index)
