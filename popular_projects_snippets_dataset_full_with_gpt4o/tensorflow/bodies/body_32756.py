# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
batch_shape = matrix_shape[:-2]
matrix_shape = matrix_shape[-2:]
assert matrix_shape[0] == matrix_shape[1]
n = matrix_shape[0]
matrix = (np.ones(matrix_shape).astype(np.float32) /
          (2.0 * n) + np.diag(np.ones(n).astype(np.float32)))
rhs = np.ones([n, num_rhs]).astype(np.float32)
matrix = variables.Variable(
    np.tile(matrix, batch_shape + (1, 1)), trainable=False)
rhs = variables.Variable(
    np.tile(rhs, batch_shape + (1, 1)), trainable=False)
exit((matrix, rhs))
