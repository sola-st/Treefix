# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [np.float32, np.float64]:
    values = [0, 1, np.nan, np.inf, np.NINF]
    x = constant_op.constant(values, dtype=dtype)
    zeros = constant_op.constant(np.zeros((5,)), dtype=dtype)
    ones = constant_op.constant(np.ones((5,)), dtype=dtype)
    with test_util.use_gpu():
        tf_result_zeros = math_ops.multiply_no_nan(x, zeros)
        self.assertAllEqual(tf_result_zeros, zeros)
        tf_result_ones = math_ops.multiply_no_nan(x, ones)
        self.assertAllEqual(tf_result_ones, x)
        # Normal floating point arithmetic if nonfinite values are in the
        # second argument.
        tf_result_reverseargs = math_ops.multiply_no_nan(zeros, x)
        self.assertAllEqual(zeros * x, tf_result_reverseargs)
