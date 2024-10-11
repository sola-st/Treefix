# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
self._verifyLogarithmComplex(np.empty([0, 2, 2], dtype=np.complex64))
self._verifyLogarithmComplex(np.empty([2, 0, 0], dtype=np.complex64))
