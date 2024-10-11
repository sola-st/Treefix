# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
self._verifyInverseReal(np.empty([0, 2, 2]))
self._verifyInverseReal(np.empty([2, 0, 0]))
