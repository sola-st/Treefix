# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
# batch_shape = [2, 2]
matrix = rng.rand(2, 3, 3)
rhs = rng.rand(2, 1, 3, 7)
matrix_broadcast = matrix + np.zeros((2, 2, 1, 1))
rhs_broadcast = rhs + np.zeros((2, 2, 1, 1))

matrix_ph = array_ops.placeholder_with_default(matrix, shape=None)
rhs_ph = array_ops.placeholder_with_default(rhs, shape=None)

result, expected = self.evaluate([
    linear_operator_util.matrix_solve_with_broadcast(matrix_ph, rhs_ph),
    linalg_ops.matrix_solve(matrix_broadcast, rhs_broadcast)
])
self.assertAllClose(expected, result)
