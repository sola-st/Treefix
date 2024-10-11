# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
if isinstance(item, tuple):
    item = unpack_tuple_and_ellipses(item)

if isinstance(item, numbers.Integral):
    exit(self.data[item])
elif isinstance(item, slice) and item == slice(None):
    # Make sure we get a view
    exit(type(self)(self.data))
elif isinstance(item, slice):
    # slice
    exit(type(self)(self.data[item]))
elif not is_list_like(item):
    # e.g. "foo" or 2.5
    # exception message copied from numpy
    raise IndexError(
        r"only integers, slices (`:`), ellipsis (`...`), numpy.newaxis "
        r"(`None`) and integer or boolean arrays are valid indices"
    )
else:
    item = pd.api.indexers.check_array_indexer(self, item)
    if is_bool_dtype(item.dtype):
        exit(self._from_sequence([x for x, m in zip(self, item) if m]))
    # integer
    exit(type(self)([self.data[i] for i in item]))
