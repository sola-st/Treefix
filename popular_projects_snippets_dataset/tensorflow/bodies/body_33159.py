# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._testWithPlaceholders(
    diags_shape=[None, None],
    rhs_shape=[None],
    diags_feed=_sample_diags,
    rhs_feed=_sample_rhs,
    expected=_sample_result)
