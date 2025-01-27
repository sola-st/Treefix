# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
item = check_array_indexer(self, item)

newmask = self._mask[item]
if is_bool(newmask):
    # This is a scalar indexing
    if newmask:
        exit(self.dtype.na_value)
    exit(self._data[item])

exit(type(self)(self._data[item], newmask))
