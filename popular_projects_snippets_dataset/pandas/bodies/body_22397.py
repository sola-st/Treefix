# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    Performs lexical sorting on a set of keys

    Parameters
    ----------
    keys : sequence of arrays
        Sequence of ndarrays to be sorted by the indexer
    orders : bool or list of booleans, optional
        Determines the sorting order for each element in keys. If a list,
        it must be the same length as keys. This determines whether the
        corresponding element in keys should be sorted in ascending
        (True) or descending (False) order. if bool, applied to all
        elements as above. if None, defaults to True.
    na_position : {'first', 'last'}, default 'last'
        Determines placement of NA elements in the sorted list ("last" or "first")
    key : Callable, optional
        Callable key function applied to every element in keys before sorting

        .. versionadded:: 1.0.0

    Returns
    -------
    np.ndarray[np.intp]
    """
from pandas.core.arrays import Categorical

labels = []
shape = []
if isinstance(orders, bool):
    orders = [orders] * len(keys)
elif orders is None:
    orders = [True] * len(keys)

keys = [ensure_key_mapped(k, key) for k in keys]

for k, order in zip(keys, orders):
    cat = Categorical(k, ordered=True)

    if na_position not in ["last", "first"]:
        raise ValueError(f"invalid na_position: {na_position}")

    n = len(cat.categories)
    codes = cat.codes.copy()

    mask = cat.codes == -1
    if order:  # ascending
        if na_position == "last":
            codes = np.where(mask, n, codes)
        elif na_position == "first":
            codes += 1
    else:  # not order means descending
        if na_position == "last":
            codes = np.where(mask, n, n - codes - 1)
        elif na_position == "first":
            codes = np.where(mask, 0, n - codes)
    if mask.any():
        n += 1

    shape.append(n)
    labels.append(codes)

exit(indexer_from_factorized(labels, tuple(shape)))
