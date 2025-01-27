# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
with self._device_scope():
    exit(super().scatter_nd_add(indices, updates, name))
