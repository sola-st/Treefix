# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
if test_util.is_xla_enabled():
    exit()
self._testWithLists(
    diags=[[2, -1, 1, 0], [1, 4, 1, -1], [0, 2, 0, 3]], rhs=[1, 2, 3, 4])
