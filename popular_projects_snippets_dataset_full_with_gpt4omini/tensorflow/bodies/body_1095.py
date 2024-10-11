# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=[[1, 2, 0, 0], [1, 3, 1, 0], [0, -1, 2, 4], [0, 0, 1, 2]],
    rhs=[[1, -1], [2, -2], [3, -3], [4, -4]],
    expected=[[-9, 9], [5, -5], [-4, 4], [4, -4]],
    diags_format="matrix")
