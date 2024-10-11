# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_lower_triangular_test.py
tril = variables_module.Variable([[1., 0.], [0., 1.]])
operator = linalg_lib.LinearOperatorLowerTriangular(
    tril, is_non_singular=True)
with self.cached_session() as sess:
    sess.run([tril.initializer])
    self.check_convert_variables_to_tensors(operator)
