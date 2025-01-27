# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_tridiag_test.py
matrix = variables_module.Variable([[3., 2., 0.], [1., 6., 4.], [0., 2, 2]])
operator = linalg_lib.LinearOperatorTridiag(
    matrix, diagonals_format='matrix')
self.check_tape_safe(operator)
