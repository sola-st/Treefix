# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Add a sequence of trackable values."""
self._check_external_modification()
super().extend(values)
self._update_snapshot()
