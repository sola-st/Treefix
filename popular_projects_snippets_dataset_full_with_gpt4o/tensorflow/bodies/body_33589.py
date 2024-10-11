# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
# 2x2 matrices
self._compareDeterminant(np.array([[2., 3.], [3., 4.]]).astype(np.float32))
self._compareDeterminant(np.array([[0., 0.], [0., 0.]]).astype(np.float32))
# 5x5 matrices (Eigen forces LU decomposition)
self._compareDeterminant(
    np.array([[2., 3., 4., 5., 6.], [3., 4., 9., 2., 0.], [
        2., 5., 8., 3., 8.
    ], [1., 6., 7., 4., 7.], [2., 3., 4., 5., 6.]]).astype(np.float32))
# A multidimensional batch of 2x2 matrices
self._compareDeterminant(np.random.rand(3, 4, 5, 2, 2).astype(np.float32))
