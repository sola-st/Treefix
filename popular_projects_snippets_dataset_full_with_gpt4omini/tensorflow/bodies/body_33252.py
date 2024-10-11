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
with self.cached_session() as sess:
    sess.run([x.initializer for x in operator.variables])
    self.check_convert_variables_to_tensors(operator)
