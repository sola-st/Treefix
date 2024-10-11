# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithPlaceholders(
    diags_shape=[None, 3, 4],
    rhs_shape=[None, 4],
    diags_feed=np.array([_sample_diags, -_sample_diags]),
    rhs_feed=np.array([_sample_rhs, 2 * _sample_rhs]),
    expected=np.array([_sample_result, -2 * _sample_result]))
