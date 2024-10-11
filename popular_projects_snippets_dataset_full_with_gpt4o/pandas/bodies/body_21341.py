# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
key = check_array_indexer(self, key)
value = self._validate_setitem_value(value)
self._ndarray[key] = value
