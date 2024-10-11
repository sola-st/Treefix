# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
self.assertAllClose(
    np.ones_like(np.diag(matrix)), np.diag(matrix), rtol=rtol)
