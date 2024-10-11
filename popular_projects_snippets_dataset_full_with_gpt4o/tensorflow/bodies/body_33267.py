# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_toeplitz_test.py
col = variables_module.Variable([1.])
row = variables_module.Variable([1.])
operator = linear_operator_toeplitz.LinearOperatorToeplitz(
    col, row, is_self_adjoint=True, is_positive_definite=True)
with self.cached_session() as sess:
    sess.run([x.initializer for x in operator.variables])
    self.check_convert_variables_to_tensors(operator)
