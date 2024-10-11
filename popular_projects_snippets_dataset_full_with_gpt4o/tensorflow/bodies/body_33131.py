# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
dummy = 20
self._test(
    diags=(_tfconst([2, 1, 4,
                     dummy]), _tfconst([1, 3, 2,
                                        2]), _tfconst([dummy, 1, -1, 1])),
    rhs=_tfconst([1, 2, 3, 4]),
    expected=_tfconst([-9, 5, -4, 4]),
    diags_format="sequence")
