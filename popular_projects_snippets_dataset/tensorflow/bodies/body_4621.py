# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
with self._device_scope():
    exit(super().assign_add(delta, use_locking, name, read_value))
