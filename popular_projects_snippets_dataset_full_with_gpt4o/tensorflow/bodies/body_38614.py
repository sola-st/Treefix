# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
with self.cached_session():
    x = constant_op.constant([], dtype=dtypes.float32, shape=[1, 4, 0])
    xt = array_ops.transpose(x, [0, 2, 1])
    self.assertAllEqual(xt.shape, (1, 0, 4))
