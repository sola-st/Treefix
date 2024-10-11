# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=[[0, 0, 0, 0], [1, 2, -1, -2], [0, 0, 0, 0]],
    rhs=[1, 2, 3, 4],
    expected=[1, 1, -3, -2])
