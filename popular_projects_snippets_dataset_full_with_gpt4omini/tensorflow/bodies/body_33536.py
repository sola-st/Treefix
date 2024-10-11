# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
multiplier = variables_module.Variable(1.23)
operator = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2, multiplier=multiplier)
with self.cached_session() as sess:
    sess.run([multiplier.initializer])
    self.check_convert_variables_to_tensors(operator)
