# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=_sample_diags,
    rhs=_sample_rhs * (1 + 1j),
    expected=_sample_result * (1 - 1j),
    conjugate_rhs=True)
