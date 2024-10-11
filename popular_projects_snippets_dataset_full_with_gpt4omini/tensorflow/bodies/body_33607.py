# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
# 2x2
identity = np.array([[1., 0], [0, 1.]])
self._verifySquareRootReal(identity)
# 3x3
identity = np.array([[1., 0, 0], [0, 1., 0], [0, 0, 1.]])
self._verifySquareRootReal(identity)
