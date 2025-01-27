# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
# Ensure that complex values are handled to be consistent with numpy
complex_ys = [([0 - 1j, 0 + 1j], dtypes.float64),
              (np.array([0 - 1j, 0 + 1j], "complex64"), dtypes.float32),
              (np.array([0 - 1j, 0 + 1j], "complex128"), dtypes.float64)]
for y, dtype in complex_ys:
    y_result = math_ops.reduce_std(y)
    self.assertEqual(np.std(y), 1.0)
    self.assertEqual(self.evaluate(y_result), 1.0)
    self.assertEqual(y_result.dtype, dtype)
