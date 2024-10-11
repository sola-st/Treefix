# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Restore the object's attributes from a name-based checkpoint."""
self._self_name_based_restores.add(checkpoint)
if self._self_update_uid < checkpoint.restore_uid:
    checkpoint.eager_restore(self)
    self._self_update_uid = checkpoint.restore_uid
