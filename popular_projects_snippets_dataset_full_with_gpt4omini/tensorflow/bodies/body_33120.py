# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
# Without partial pivoting (e.g. Thomas algorithm) this would fail.
self._testWithLists(
    diags=[[2, -1, 1, 0], [1, 4, 1, -1], [0, 2, -2, 3]],
    rhs=[1, 2, 3, 4],
    expected=[8, -3.5, 0, -4])
