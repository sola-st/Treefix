# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=_sample_diags,
    rhs=_sample_rhs,
    expected=_sample_result,
    transpose_rhs=True)
