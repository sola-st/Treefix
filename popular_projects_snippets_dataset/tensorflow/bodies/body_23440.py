# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Add a new trackable value."""
self._check_external_modification()
super().append(value)
self._update_snapshot()
