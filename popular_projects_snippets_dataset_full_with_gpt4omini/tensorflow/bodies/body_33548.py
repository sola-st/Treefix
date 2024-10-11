# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_tridiag_test.py
diag = variables_module.Variable([[3., 6., 2.], [2., 4., 2.], [5., 1., 2.]])
operator = linalg_lib.LinearOperatorTridiag(
    diag, diagonals_format='compact')
self.check_tape_safe(operator)
