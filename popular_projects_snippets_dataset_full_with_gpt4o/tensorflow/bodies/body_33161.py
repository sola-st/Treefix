# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithPlaceholders(
    diags_shape=[3, 4],
    rhs_shape=[4, None],
    diags_feed=_sample_diags,
    rhs_feed=np.transpose([_sample_rhs, 2 * _sample_rhs]),
    expected=np.transpose([_sample_result, 2 * _sample_result]))
