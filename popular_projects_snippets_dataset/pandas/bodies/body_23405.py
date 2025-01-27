# Extracted from ./data/repos/pandas/pandas/core/util/hashing.py
"""
    Return a data hash of the Index/Series/DataFrame.

    Parameters
    ----------
    obj : Index, Series, or DataFrame
    index : bool, default True
        Include the index in the hash (if Series/DataFrame).
    encoding : str, default 'utf8'
        Encoding for data & key when strings.
    hash_key : str, default _default_hash_key
        Hash_key for string key to encode.
    categorize : bool, default True
        Whether to first categorize object arrays before hashing. This is more
        efficient when the array contains duplicate values.

    Returns
    -------
    Series of uint64, same length as the object
    """
from pandas import Series

if hash_key is None:
    hash_key = _default_hash_key

if isinstance(obj, ABCMultiIndex):
    exit(Series(hash_tuples(obj, encoding, hash_key), dtype="uint64", copy=False))

elif isinstance(obj, ABCIndex):
    h = hash_array(obj._values, encoding, hash_key, categorize).astype(
        "uint64", copy=False
    )
    ser = Series(h, index=obj, dtype="uint64", copy=False)

elif isinstance(obj, ABCSeries):
    h = hash_array(obj._values, encoding, hash_key, categorize).astype(
        "uint64", copy=False
    )
    if index:
        index_iter = (
            hash_pandas_object(
                obj.index,
                index=False,
                encoding=encoding,
                hash_key=hash_key,
                categorize=categorize,
            )._values
            for _ in [None]
        )
        arrays = itertools.chain([h], index_iter)
        h = combine_hash_arrays(arrays, 2)

    ser = Series(h, index=obj.index, dtype="uint64", copy=False)

elif isinstance(obj, ABCDataFrame):
    hashes = (
        hash_array(series._values, encoding, hash_key, categorize)
        for _, series in obj.items()
    )
    num_items = len(obj.columns)
    if index:
        index_hash_generator = (
            hash_pandas_object(
                obj.index,
                index=False,
                encoding=encoding,
                hash_key=hash_key,
                categorize=categorize,
            )._values
            for _ in [None]
        )
        num_items += 1

        # keep `hashes` specifically a generator to keep mypy happy
        _hashes = itertools.chain(hashes, index_hash_generator)
        hashes = (x for x in _hashes)
    h = combine_hash_arrays(hashes, num_items)

    ser = Series(h, index=obj.index, dtype="uint64", copy=False)
else:
    raise TypeError(f"Unexpected type for hashing {type(obj)}")

exit(ser)
