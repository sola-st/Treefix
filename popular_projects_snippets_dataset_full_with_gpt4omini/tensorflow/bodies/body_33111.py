# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=[[2, -1, 0], [1, 3, 1], [0, -1, -2]],
    rhs=[1, 2, 3],
    expected=[-3, 2, 7])
