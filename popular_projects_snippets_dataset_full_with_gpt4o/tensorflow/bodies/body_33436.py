# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
base_operator = linalg.LinearOperatorDiag(
    variables_module.Variable([1.], name="diag"),
    is_positive_definite=True,
    is_self_adjoint=True)

operator = linalg.LinearOperatorLowRankUpdate(
    base_operator,
    u=variables_module.Variable([[2.]], name="u"),
    v=variables_module.Variable([[1.25]], name="v")
    if self._use_v else None,
    diag_update=variables_module.Variable([1.25], name="diag_update")
    if self._use_diag_update else None,
    is_diag_update_positive=self._is_diag_update_positive)
with self.cached_session() as sess:
    sess.run([x.initializer for x in operator.variables])
    self.check_convert_variables_to_tensors(operator)
