# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._test(
    _tfconst(diags), _tfconst(rhs), _tfconst(expected), diags_format,
    transpose_rhs, conjugate_rhs)
