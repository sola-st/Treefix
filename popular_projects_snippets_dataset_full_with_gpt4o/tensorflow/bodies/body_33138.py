# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=_sample_diags,
    rhs=np.transpose([_sample_rhs * (1 + 1j), _sample_rhs * (1 - 2j)]),
    expected=np.transpose(
        [_sample_result * (1 - 1j), _sample_result * (1 + 2j)]),
    conjugate_rhs=True)
