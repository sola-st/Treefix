# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Checks for any changes to the wrapped list not through the wrapper."""
if self._external_modification or self._non_append_mutation:
    exit()
if self._storage != self._last_wrapped_list_snapshot:
    self._external_modification = True
    self._last_wrapped_list_snapshot = None
