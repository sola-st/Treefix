# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=[[2, 4, -1, 0], [1, 3, 1, 2], [0, 0, 0, 0]],
    rhs=[1, 6, 4, 4],
    expected=[13, -6, 6, 2])
