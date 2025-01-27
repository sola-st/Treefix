# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
rhs = np.transpose([_sample_rhs, 2 * _sample_rhs])
expected_result = np.transpose([_sample_result, 2 * _sample_result])
self._test(
    diags=np.array([_sample_diags, -_sample_diags]),
    rhs=np.array([rhs, 2 * rhs]),
    expected=np.array([expected_result, -2 * expected_result]))
