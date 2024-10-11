# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._gradientTest(
    _tfconst(diags), _tfconst(rhs), _tfconst(y), expected_grad_diags,
    expected_grad_rhs, diags_format, transpose_rhs, conjugate_rhs)
