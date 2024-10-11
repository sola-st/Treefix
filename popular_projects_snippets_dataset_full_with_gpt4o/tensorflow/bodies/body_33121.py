# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=[[2, 1, -1, 0], [1, -1, 2, 1], [0, 1, -6, 1]],
    rhs=[1, 2, -1, -2],
    expected=[5, -2, -5, 3])
