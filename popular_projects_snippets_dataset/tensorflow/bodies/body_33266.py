# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_toeplitz_test.py
col = variables_module.Variable([1.])
row = variables_module.Variable([1.])
operator = linear_operator_toeplitz.LinearOperatorToeplitz(
    col, row, is_self_adjoint=True, is_positive_definite=True)
self.check_tape_safe(
    operator,
    skip_options=[
        # .diag_part, .trace depend only on `col`, so test explicitly below.
        linear_operator_test_util.CheckTapeSafeSkipOptions.DIAG_PART,
        linear_operator_test_util.CheckTapeSafeSkipOptions.TRACE,
    ])

with backprop.GradientTape() as tape:
    self.assertIsNotNone(tape.gradient(operator.diag_part(), col))

with backprop.GradientTape() as tape:
    self.assertIsNotNone(tape.gradient(operator.trace(), col))
