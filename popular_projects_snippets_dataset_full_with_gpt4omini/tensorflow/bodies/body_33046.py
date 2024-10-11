# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
matrix = [[11., 0.], [1., 8.]]
operator_1 = linalg.LinearOperatorFullMatrix(matrix, name="left")
operator_2 = linalg.LinearOperatorFullMatrix(matrix, name="right")

operator = kronecker.LinearOperatorKronecker([operator_1, operator_2])

self.assertEqual("left_x_right", operator.name)
