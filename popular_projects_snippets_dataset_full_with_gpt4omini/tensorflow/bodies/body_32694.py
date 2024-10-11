# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
# These cannot be done in the automated (base test class) tests since they
# test shapes that tf.matmul cannot handle.
# In particular, tf.matmul does not broadcast.
with self.cached_session() as sess:
    x = random_ops.random_normal(shape=(2, 2, 3, 4))

    # This LinearOperatorDiag will be broadcast to (2, 2, 3, 3) during solve
    # and matmul with 'x' as the argument.
    diag = random_ops.random_uniform(shape=(2, 1, 3))
    operator = linalg.LinearOperatorDiag(diag, is_self_adjoint=True)
    self.assertAllEqual((2, 1, 3, 3), operator.shape)

    # Create a batch matrix with the broadcast shape of operator.
    diag_broadcast = array_ops.concat((diag, diag), 1)
    mat = array_ops.matrix_diag(diag_broadcast)
    self.assertAllEqual((2, 2, 3, 3), mat.shape)  # being pedantic.

    operator_matmul = operator.matmul(x)
    mat_matmul = math_ops.matmul(mat, x)
    self.assertAllEqual(operator_matmul.shape, mat_matmul.shape)
    self.assertAllClose(*self.evaluate([operator_matmul, mat_matmul]))

    operator_solve = operator.solve(x)
    mat_solve = linalg_ops.matrix_solve(mat, x)
    self.assertAllEqual(operator_solve.shape, mat_solve.shape)
    self.assertAllClose(*self.evaluate([operator_solve, mat_solve]))
