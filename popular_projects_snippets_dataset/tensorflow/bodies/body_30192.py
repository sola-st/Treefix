# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
res = array_ops.sequence_mask(constant_op.constant([[1, 3, 2]]), 5)
self.assertAllEqual(res.get_shape(), [1, 3, 5])
self.assertAllEqual(
    res,
    [[[True, False, False, False, False], [True, True, True, False, False],
      [True, True, False, False, False]]])

# test dtype and default maxlen:
res = array_ops.sequence_mask(
    constant_op.constant([[0, 1, 4], [1, 2, 3]]), dtype=dtypes.float32)
self.assertAllEqual(res.get_shape().as_list(), [2, 3, 4])
self.assertAllEqual(
    res,
    [[[0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [1.0, 1.0, 1.0, 1.0]],
     [[1.0, 0.0, 0.0, 0.0], [1.0, 1.0, 0.0, 0.0], [1.0, 1.0, 1.0, 0.0]]])
