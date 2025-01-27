# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_inversion_test.py
matrix = variables_module.Variable([[1., 2.], [3., 4.]])
operator = LinearOperatorInversion(linalg.LinearOperatorFullMatrix(matrix))
self.check_tape_safe(operator)
