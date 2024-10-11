# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
for np_type in [np.complex64, np.complex128]:
    self._verifySquareRoot(x, np_type)
