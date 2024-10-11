# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
self._verifyCholesky(np.empty([0, 2, 2]))
self._verifyCholesky(np.empty([2, 0, 0]))
