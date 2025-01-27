# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Add a new trackable value."""
value = self._track_value(value, self._name_element(len(self._storage)))
self._storage.append(value)
