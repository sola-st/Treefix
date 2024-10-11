# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
np.random.seed(seed)
data = np.random.normal(size=(batch_size, m, 3 + n))
exit((variables.Variable(data[:, :, 0], dtype=dtypes.float64),
        variables.Variable(data[:, :, 1], dtype=dtypes.float64),
        variables.Variable(data[:, :, 2], dtype=dtypes.float64),
        variables.Variable(data[:, :, 3:], dtype=dtypes.float64)))
