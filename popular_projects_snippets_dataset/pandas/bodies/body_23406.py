# Extracted from ./data/repos/pandas/pandas/core/util/hashing.py
"""
    Hash an MultiIndex / listlike-of-tuples efficiently.

    Parameters
    ----------
    vals : MultiIndex or listlike-of-tuples
    encoding : str, default 'utf8'
    hash_key : str, default _default_hash_key

    Returns
    -------
    ndarray[np.uint64] of hashed values
    """
if not is_list_like(vals):
    raise TypeError("must be convertible to a list-of-tuples")

from pandas import (
    Categorical,
    MultiIndex,
)

if not isinstance(vals, ABCMultiIndex):
    mi = MultiIndex.from_tuples(vals)
else:
    mi = vals

# create a list-of-Categoricals
cat_vals = [
    Categorical(mi.codes[level], mi.levels[level], ordered=False, fastpath=True)
    for level in range(mi.nlevels)
]

# hash the list-of-ndarrays
hashes = (
    _hash_categorical(cat, encoding=encoding, hash_key=hash_key) for cat in cat_vals
)
h = combine_hash_arrays(hashes, len(cat_vals))

exit(h)
