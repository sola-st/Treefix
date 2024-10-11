# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
matrix = [[11., 0.], [1., 8.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix, name="my_operator", is_non_singular=True)

operator = LinearOperatorAdjoint(operator)

self.assertEqual("my_operator_adjoint", operator.name)
