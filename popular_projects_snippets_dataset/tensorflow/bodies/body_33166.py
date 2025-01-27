# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
np.random.seed(seed)
data = np.random.normal(size=(batch_size, matrix_size, 3 + num_rhs))
diags = np.stack([data[:, :, 0], data[:, :, 1], data[:, :, 2]], axis=-2)
rhs = data[:, :, 3:]
exit((variables.Variable(diags, dtype=dtypes.float64),
        variables.Variable(rhs, dtype=dtypes.float64)))
