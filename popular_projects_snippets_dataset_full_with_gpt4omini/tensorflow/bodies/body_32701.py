# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
diag = variables_module.Variable([[2.]])
operator = linalg.LinearOperatorDiag(diag)
with self.cached_session() as sess:
    sess.run([diag.initializer])
    self.check_convert_variables_to_tensors(operator)
