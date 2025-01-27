# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=[[2, 4, -1, 0], [1, 3, 1, 2], [0, 0, 0, 0]],
    rhs=[1, 6, 4, 4],
    expected=[13, -6, 6, 2])
