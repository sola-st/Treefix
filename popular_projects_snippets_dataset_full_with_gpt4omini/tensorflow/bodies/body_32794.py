# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
operator = linalg.LinearOperatorFullMatrix(
    np.float64([[1., 0.5], [0.5, 1.]]),
    is_square=True,
    is_self_adjoint=True,
    is_non_singular=True,
    is_positive_definite=True)
rhs = np.random.uniform(-1., 1., size=[3, 2, 2])
for adjoint in [False, True]:
    for adjoint_arg in [False, True]:
        op_val = operator.matmul(
            rhs, adjoint=adjoint, adjoint_arg=adjoint_arg)
        matmul_val = math_ops.matmul(
            operator, rhs, adjoint_a=adjoint, adjoint_b=adjoint_arg)
        self.assertAllClose(
            self.evaluate(op_val), self.evaluate(matmul_val))

    op_val = operator.solve(rhs, adjoint=adjoint)
    solve_val = linalg.solve(operator, rhs, adjoint=adjoint)
    self.assertAllClose(
        self.evaluate(op_val), self.evaluate(solve_val))
