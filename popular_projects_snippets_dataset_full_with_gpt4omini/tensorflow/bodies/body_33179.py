# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
matrix = variables_module.Variable([[2.]])
operator = linalg.LinearOperatorFullMatrix(matrix)
self.check_tape_safe(operator)
