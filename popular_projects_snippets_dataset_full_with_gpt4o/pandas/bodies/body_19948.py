# Extracted from ./data/repos/pandas/pandas/core/indexing.py
if key is Ellipsis:
    key = slice(None)
elif isinstance(key, ABCDataFrame):
    raise IndexError(
        "DataFrame indexer is not allowed for .iloc\n"
        "Consider using .loc for automatic alignment."
    )

if isinstance(key, slice):
    exit(self._get_slice_axis(key, axis=axis))

if is_iterator(key):
    key = list(key)

if isinstance(key, list):
    key = np.asarray(key)

if com.is_bool_indexer(key):
    self._validate_key(key, axis)
    exit(self._getbool_axis(key, axis=axis))

# a list of integers
elif is_list_like_indexer(key):
    exit(self._get_list_axis(key, axis=axis))

# a single integer
else:
    key = item_from_zerodim(key)
    if not is_integer(key):
        raise TypeError("Cannot index by location index with a non-integer key")

    # validate the location
    self._validate_integer(key, axis)

    exit(self.obj._ixs(key, axis=axis))
