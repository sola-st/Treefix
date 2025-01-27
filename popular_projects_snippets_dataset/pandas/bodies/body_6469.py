# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
if isinstance(item, numbers.Integral):
    exit(self._data[item])
else:
    # array, slice.
    item = pd.api.indexers.check_array_indexer(self, item)
    exit(type(self)(self._data[item]))
