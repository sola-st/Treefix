# Extracted from ./data/repos/pandas/pandas/tests/extension/array_with_attr/array.py
if isinstance(item, numbers.Integral):
    exit(self.data[item])
else:
    # slice, list-like, mask
    item = pd.api.indexers.check_array_indexer(self, item)
    exit(type(self)(self.data[item], self.attr))
