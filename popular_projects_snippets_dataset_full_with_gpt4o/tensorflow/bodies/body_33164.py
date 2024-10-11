# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
if context.executing_eagerly():
    exit()

def test_with_matrix_shapes(matrix_shape, rhs_shape=None):
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

test_with_matrix_shapes(matrix_shape=[4, 4], rhs_shape=[None, None])
test_with_matrix_shapes(matrix_shape=[None, 4], rhs_shape=[None, None])
test_with_matrix_shapes(matrix_shape=[4, None], rhs_shape=[None, None])
test_with_matrix_shapes(matrix_shape=[None, None], rhs_shape=[None, None])
test_with_matrix_shapes(matrix_shape=[4, 4])
test_with_matrix_shapes(matrix_shape=[None, 4])
test_with_matrix_shapes(matrix_shape=[4, None])
test_with_matrix_shapes(matrix_shape=[None, None])
test_with_matrix_shapes(matrix_shape=None, rhs_shape=[None, None])
test_with_matrix_shapes(matrix_shape=None)
