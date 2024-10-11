# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
mat = np.float64([[1., 0.5], [0.5, 1.]])
right_operator = linalg.LinearOperatorFullMatrix(
    mat,
    is_square=True,
    is_self_adjoint=True,
    is_non_singular=True,
    is_positive_definite=True)
lhs = np.random.uniform(-1., 1., size=[3, 2, 2])

for adjoint in [False, True]:
    for adjoint_arg in [False, True]:
        op_val = math_ops.matmul(
            lhs, mat, adjoint_a=adjoint, adjoint_b=adjoint_arg)
        matmul_val = math_ops.matmul(
            lhs, right_operator, adjoint_a=adjoint, adjoint_b=adjoint_arg)
        self.assertAllClose(
            self.evaluate(op_val), self.evaluate(matmul_val))
