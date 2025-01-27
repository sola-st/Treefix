# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
matrix = np.array([[1, 2, 0, 0], [1, 3, 1, 0], [0, -1, 2, 4],
                   [0, 0, 1, 2]])
rhs = np.array([1, 2, 3, 4])
x = np.array([-9, 5, -4, 4])
self._testWithPlaceholders(
    diags_shape=matrix_shape,
    rhs_shape=rhs_shape,
    diags_feed=matrix,
    rhs_feed=np.transpose([rhs, 2 * rhs]),
    expected=np.transpose([x, 2 * x]),
    diags_format="matrix")
