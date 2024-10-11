# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_tridiag_test.py
diagonals = [
    variables_module.Variable([3., 6., 2.]),
    variables_module.Variable([2., 4., 2.]),
    variables_module.Variable([5., 1., 2.])]
operator = linalg_lib.LinearOperatorTridiag(
    diagonals, diagonals_format='sequence')
# Skip the diagonal part and trace since this only dependent on the
# middle variable. We test this below.
self.check_tape_safe(operator, skip_options=['diag_part', 'trace'])

diagonals = [
    [3., 6., 2.],
    variables_module.Variable([2., 4., 2.]),
    [5., 1., 2.]
]
operator = linalg_lib.LinearOperatorTridiag(
    diagonals, diagonals_format='sequence')
