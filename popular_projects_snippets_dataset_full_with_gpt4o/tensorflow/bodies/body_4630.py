# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
with self._device_scope():
    exit(super().batch_scatter_update(sparse_delta, use_locking, name))
