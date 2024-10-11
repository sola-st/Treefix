# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.random.rand(2, 2).astype(np.float32)
coeffs = []
np_val = np.polyval(coeffs, x)
with self.cached_session():
    tf_val = math_ops.polyval(coeffs, x)
    self.assertAllClose(np_val, self.evaluate(tf_val))
