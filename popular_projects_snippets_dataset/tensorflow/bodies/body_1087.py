# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=_sample_diags,
    rhs=np.transpose([_sample_rhs, 2 * _sample_rhs]),
    expected=np.transpose([_sample_result, 2 * _sample_result]))
