# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_inversion_test.py
matrix = [[11., 0.], [1., 8.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix, name="my_operator", is_non_singular=True)

operator = LinearOperatorInversion(operator)

self.assertEqual("my_operator_inv", operator.name)
