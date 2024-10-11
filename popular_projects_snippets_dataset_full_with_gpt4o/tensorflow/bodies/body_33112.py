# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=[[2, 0], [1, 3], [0, 1]], rhs=[1, 4], expected=[-5, 3])
