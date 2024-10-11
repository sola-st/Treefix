# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
batch_shape = matrix_shape[:-2]
matrix_shape = matrix_shape[-2:]
m = matrix_shape[-2]
np.random.seed(1)
matrix = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(matrix_shape)).reshape(matrix_shape).astype(np.float32)
rhs = np.ones([m, num_rhs]).astype(np.float32)
matrix = variables.Variable(
    np.tile(matrix, batch_shape + (1, 1)), trainable=False)
rhs = variables.Variable(np.tile(rhs, batch_shape + (1, 1)), trainable=False)
exit((matrix, rhs))
