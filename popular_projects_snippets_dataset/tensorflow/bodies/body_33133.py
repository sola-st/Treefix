# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=[[1, 2, 0, 0], [1, 3, 1, 0], [0, -1, 2, 4], [0, 0, 1, 2]],
    rhs=[1, 2, 3, 4],
    expected=[-9, 5, -4, 4],
    diags_format="matrix")
