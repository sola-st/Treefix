# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_householder_test.py
reflection_axis = variables_module.Variable([1., 3., 5., 8.])
operator = householder.LinearOperatorHouseholder(reflection_axis)
self.check_tape_safe(
    operator,
    skip_options=[
        # Determinant hard-coded as 1.
        CheckTapeSafeSkipOptions.DETERMINANT,
        CheckTapeSafeSkipOptions.LOG_ABS_DETERMINANT,
        # Trace hard-coded.
        CheckTapeSafeSkipOptions.TRACE,
    ])
