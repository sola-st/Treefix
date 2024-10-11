# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Construct a new sequence. Arguments are passed to `dict()`."""
super().__init__()
self._storage = self._make_storage(*args, **kwargs)
self._storage.update(
    {key: self._track_value(
        value, name=self._name_element(key))
     for key, value in self._storage.items()})
