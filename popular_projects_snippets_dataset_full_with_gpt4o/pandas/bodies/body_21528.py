# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
value_left, value_right = self._validate_setitem_value(value)
key = check_array_indexer(self, key)

self._left[key] = value_left
self._right[key] = value_right
