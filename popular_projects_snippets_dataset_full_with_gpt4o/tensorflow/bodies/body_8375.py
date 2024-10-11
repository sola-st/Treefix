# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Copies a tensor or IndexedSlices to a device."""
with ops.device(device):
    if isinstance(value, indexed_slices.IndexedSlices):
        copied_values = array_ops.identity(value.values)
        copied_indices = array_ops.identity(value.indices)
        if value.dense_shape is not None:
            copied_shape = array_ops.identity(value.dense_shape)
        else:
            copied_shape = None
        result = indexed_slices.IndexedSlices(copied_values, copied_indices,
                                              copied_shape)
    else:
        result = array_ops.identity(value)
exit(result)
