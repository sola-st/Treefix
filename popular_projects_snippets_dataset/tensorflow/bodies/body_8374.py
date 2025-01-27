# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
if isinstance(value, indexed_slices.IndexedSlices):
    value = backprop_util.FlattenNestedIndexedSlices(value)
    exit(indexed_slices.IndexedSlices(value.values / n, value.indices,
                                        value.dense_shape))
else:
    exit(value / n)
