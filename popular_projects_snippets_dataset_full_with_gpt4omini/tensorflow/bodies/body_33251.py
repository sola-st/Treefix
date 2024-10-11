# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
operator_1 = linalg.LinearOperatorFullMatrix(
    variables_module.Variable([[1., 0.], [0., 1.]]),
    is_self_adjoint=True,
    is_positive_definite=True)
operator_2 = linalg.LinearOperatorFullMatrix(
    variables_module.Variable([[2., 0.], [1., 0.]]))
operator_3 = linalg.LinearOperatorFullMatrix(
    variables_module.Variable([[3., 1.], [1., 3.]]),
    is_self_adjoint=True,
    is_positive_definite=True)
operator = block_lower_triangular.LinearOperatorBlockLowerTriangular(
    [[operator_1], [operator_2, operator_3]],
    is_self_adjoint=False,
    is_positive_definite=True)

diagonal_grads_only = ["diag_part", "trace", "determinant",
                       "log_abs_determinant"]
self.check_tape_safe(operator, skip_options=diagonal_grads_only)

for y in diagonal_grads_only:
    for diag_block in [operator_1, operator_3]:
        with backprop.GradientTape() as tape:
            grads = tape.gradient(getattr(operator, y)(), diag_block.variables)
            for item in grads:
                self.assertIsNotNone(item)
