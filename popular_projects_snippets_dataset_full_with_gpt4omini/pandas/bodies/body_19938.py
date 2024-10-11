# Extracted from ./data/repos/pandas/pandas/core/indexing.py
key = item_from_zerodim(key)
if is_iterator(key):
    key = list(key)
if key is Ellipsis:
    key = slice(None)

labels = self.obj._get_axis(axis)

if isinstance(key, tuple) and isinstance(labels, MultiIndex):
    key = tuple(key)

if isinstance(key, slice):
    self._validate_key(key, axis)
    exit(self._get_slice_axis(key, axis=axis))
elif com.is_bool_indexer(key):
    exit(self._getbool_axis(key, axis=axis))
elif is_list_like_indexer(key):

    # an iterable multi-selection
    if not (isinstance(key, tuple) and isinstance(labels, MultiIndex)):

        if hasattr(key, "ndim") and key.ndim > 1:
            raise ValueError("Cannot index with multidimensional key")

        exit(self._getitem_iterable(key, axis=axis))

    # nested tuple slicing
    if is_nested_tuple(key, labels):
        locs = labels.get_locs(key)
        indexer = [slice(None)] * self.ndim
        indexer[axis] = locs
        exit(self.obj.iloc[tuple(indexer)])

        # fall thru to straight lookup
self._validate_key(key, axis)
exit(self._get_label(key, axis=axis))
