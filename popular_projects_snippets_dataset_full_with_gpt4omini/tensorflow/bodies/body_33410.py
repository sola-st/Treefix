# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
# Since the second arg has extra dims, and the domain dim of the first arg
# is larger than the number of linear equations, code will "flip" the extra
# dims of the first arg to the far right, making extra linear equations
# (then call the matrix function, then flip back).
# We have verified that this optimization indeed happens.  How? We stepped
# through with a debugger.
# batch_shape = [2]
matrix = rng.rand(3, 3)
rhs = rng.rand(2, 3, 2)
matrix_broadcast = matrix + np.zeros((2, 1, 1))

result = linear_operator_util.matrix_solve_with_broadcast(
    matrix, rhs, adjoint=True)
self.assertAllEqual((2, 3, 2), result.shape)
expected = linalg_ops.matrix_solve(matrix_broadcast, rhs, adjoint=True)
self.assertAllClose(*self.evaluate([expected, result]))
