# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
for np_type in [np.complex64, np.complex128]:
    self._verifyLogarithm(x, np_type)
