# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
self.assertAllClose(np.zeros_like(matrix.imag), matrix.imag, atol=tol)
self.assertAllClose(matrix.real, matrix.real.T, rtol=tol)
