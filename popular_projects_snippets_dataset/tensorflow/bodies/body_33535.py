# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
multiplier = variables_module.Variable(1.23)
operator = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2, multiplier=multiplier)
self.check_tape_safe(operator)
