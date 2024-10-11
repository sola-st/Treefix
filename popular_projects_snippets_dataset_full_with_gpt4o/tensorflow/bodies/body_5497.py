# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
with ops.device(device):
    tensor = indexed_slices_lib.IndexedSlices(
        values=constant_op.constant(values),
        indices=constant_op.constant(indices),
        dense_shape=constant_op.constant(dense_shape))
exit(tensor)
