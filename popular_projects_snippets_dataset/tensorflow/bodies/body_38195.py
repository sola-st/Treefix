# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.random.rand(2, 2).astype(dtype)
coeffs = [np.random.rand(2, 2).astype(dtype) for _ in range(degree + 1)]
np_val = np.polyval(coeffs, x)
with self.cached_session():
    tf_val = math_ops.polyval(coeffs, x)
    self.assertAllClose(np_val, self.evaluate(tf_val))
