# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
self._verifyLu(np.empty([0, 2, 2]))
self._verifyLu(np.empty([2, 0, 0]))
