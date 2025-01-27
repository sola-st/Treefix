# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
matrix = variables_module.Variable([[1., 2.], [3., 4.]])
operator = LinearOperatorAdjoint(linalg.LinearOperatorFullMatrix(matrix))
self.check_tape_safe(operator)
