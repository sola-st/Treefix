# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
# test dtype and default maxlen:
res = array_ops.sequence_mask(
    constant_op.constant([0, 1, 4]), dtype=dtypes.float32)
self.assertAllEqual(res.get_shape().as_list(), [3, 4])
self.assertAllEqual(
    res, [[0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [1.0, 1.0, 1.0, 1.0]])
