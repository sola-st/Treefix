# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for dtype in [dtypes.int64, dtypes.int32]:
    with self.cached_session():
        v = math_ops.reduce_min([0, 0], constant_op.constant(0, dtype=dtype))
        tf_v = self.evaluate(v)
    self.assertAllEqual(tf_v, 0)
