# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=[[0, 0, 0, 0], [2, -1, 3, 1], [0, 1, 4, 2]],
    rhs=[4, 5, 6, 1],
    expected=[2, -3, 6, -11])
