# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=[[[1, 2, 0, 0], [1, 3, 1, 0], [0, -1, 2, 4], [0, 0, 1, 2]],
           [[-1, -2, 0, 0], [-1, -3, -1, 0], [0, 1, -2, -4], [0, 0, -1,
                                                              -2]]],
    rhs=[[1, 2, 3, 4], [1, 2, 3, 4]],
    expected=[[-9, 5, -4, 4], [9, -5, 4, -4]],
    diags_format="matrix")
