# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
diag = variables_module.Variable([[2.]])
operator = linalg.LinearOperatorDiag(diag)
self.check_tape_safe(operator)
