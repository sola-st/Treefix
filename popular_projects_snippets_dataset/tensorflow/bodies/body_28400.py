# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
# Introduce an incorrect padded shape that cannot (currently) be
# detected at graph construction time.
exit(xs.padded_batch(
    4,
    padded_shapes=(tensor_shape.TensorShape([]),
                   constant_op.constant([5], dtype=dtypes.int64) * -1)))
