# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
with self.cached_session():
    x = constant_op.constant(42, dtype=dtypes.float32, shape=[])
    xt = array_ops.transpose(x)
    self.assertAllEqual(xt, x)
