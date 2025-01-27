# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=np.array([_sample_diags, -_sample_diags]),
    rhs=np.array([_sample_rhs, 2 * _sample_rhs]),
    expected=np.array([_sample_result, -2 * _sample_result]),
    transpose_rhs=True)
