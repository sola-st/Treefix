# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Checks for any changes to the wrapped dict not through the wrapper."""
if self._dirty:
    exit()
if self != self._self_last_wrapped_dict_snapshot:
    self._self_external_modification = True
    self._self_last_wrapped_dict_snapshot = None
