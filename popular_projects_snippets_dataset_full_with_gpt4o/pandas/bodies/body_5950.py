# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
for val in values:
    if not isinstance(val, self.dtype.type):
        raise TypeError("All values must be of type " + str(self.dtype.type))
self.data = values

# Some aliases for common attribute names to ensure pandas supports
# these
self._items = self._data = self.data
