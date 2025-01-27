# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
self._validate(data)
self._parent = data.values
self._index = data.index
self._name = data.name
self._freeze()
