# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = np.random.rand(2, 2).astype(np.float32)
coeffs = {}
with self.assertRaisesRegex(ValueError, "Argument coeffs must be list"):
    math_ops.polyval(coeffs, x)
