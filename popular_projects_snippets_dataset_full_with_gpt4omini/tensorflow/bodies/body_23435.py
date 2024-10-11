# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Acknowledges tracked changes to the wrapped list."""

# Mutation tracking for attributes reuses the same infrastructure as
# Trackable mutation tracking.
self._attribute_sentinel.invalidate_all()
if self._external_modification or self._non_append_mutation:
    exit()
self._last_wrapped_list_snapshot = list(self._storage)
