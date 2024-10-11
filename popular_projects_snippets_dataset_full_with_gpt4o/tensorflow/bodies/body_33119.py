# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
if test_util.is_xla_enabled():
    # XLA implementation does not check invertibility.
    exit()
self._testWithLists(diags=[[3, 0], [1, 3], [0, 1]], rhs=[1, 4])
