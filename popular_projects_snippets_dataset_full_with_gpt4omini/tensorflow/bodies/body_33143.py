# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithLists(
    diags=np.array([_sample_diags, -_sample_diags]),
    rhs=np.array([_sample_rhs, 2 * _sample_rhs]),
    expected=np.array([_sample_result, -2 * _sample_result]),
    transpose_rhs=True)
