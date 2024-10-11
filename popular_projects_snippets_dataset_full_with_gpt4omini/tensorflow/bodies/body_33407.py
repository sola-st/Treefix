# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
# batch_shape = [2]
matrix = rng.rand(2, 3, 3)
rhs = rng.rand(3, 7)
rhs_broadcast = rhs + np.zeros((2, 1, 1))

result = linear_operator_util.matrix_solve_with_broadcast(matrix, rhs)
self.assertAllEqual((2, 3, 7), result.shape)
expected = linalg_ops.matrix_solve(matrix, rhs_broadcast)
self.assertAllClose(*self.evaluate([expected, result]))
