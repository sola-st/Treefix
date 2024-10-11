# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
np.random.seed(seed)
import scipy.sparse as sparse  # pylint:disable=g-import-not-at-top
# By being strictly diagonally dominant, we guarantee invertibility.d
diag = 2 * np.abs(np.random.randn(matrix_size)) + 4.1
subdiag = 2 * np.abs(np.random.randn(matrix_size - 1))
superdiag = 2 * np.abs(np.random.randn(matrix_size - 1))
matrix = sparse.diags([superdiag, diag, subdiag], [1, 0, -1]).toarray()
vector = np.random.randn(batch_size, matrix_size, num_rhs)
exit((variables.Variable(np.tile(matrix, (batch_size, 1, 1))),
        variables.Variable(vector)))
