# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._testWithDiagonalLists(
    diags=[[2, 1, 4], [1, 3, 2, 2], [1, -1, 1]],
    rhs=[1, 2, 3, 4],
    expected=[-9, 5, -4, 4],
    diags_format="sequence")
