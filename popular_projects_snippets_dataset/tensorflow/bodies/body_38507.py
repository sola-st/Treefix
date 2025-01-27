# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
np_ans = np_func(x)
with test_util.use_gpu():
    result = tf_func(ops.convert_to_tensor(x))
    tf_gpu = self.evaluate(result)
    # Slightly increase the tolerance for float64 computations. This is
    # desired for specifically lgamma but shouldn't be of concern for other
    # functions.
    self.assertAllCloseAccordingToType(np_ans, tf_gpu, atol=2e-6)
