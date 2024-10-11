# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for dtype in [dtypes.int64, dtypes.int32]:
    with self.session():
        v = math_ops.reduce_any([True, True],
                                constant_op.constant(0, dtype=dtype))
        tf_v = self.evaluate(v)
    self.assertAllEqual(tf_v, True)
