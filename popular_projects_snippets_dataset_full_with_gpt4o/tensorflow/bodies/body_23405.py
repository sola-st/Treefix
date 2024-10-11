# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Construct a new sequence. Arguments are passed to `list()`."""
super().__init__()
self._storage = self._make_storage(*args, **kwargs)
for index, element in enumerate(self._storage):
    self._storage[index] = self._track_value(
        element, name=self._name_element(index))
