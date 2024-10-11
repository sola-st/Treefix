# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=[[2, 0], [1, 3], [0, 1]],
    rhs=[[1, 2, 3], [4, 8, 12]],
    expected=[[-5, -10, -15], [3, 6, 9]])
