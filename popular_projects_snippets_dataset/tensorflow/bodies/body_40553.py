# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
# Fill requires the first input to be an int32 tensor.
self.assertAllEqual(
    [1.0, 1.0],
    array_ops.fill(constant_op.constant([2], dtype=dtypes.int64),
                   constant_op.constant(1)))
