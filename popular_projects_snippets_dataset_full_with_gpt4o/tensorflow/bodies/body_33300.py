# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_householder_test.py
reflection_axis = variables_module.Variable([1., 3., 5., 8.])
operator = householder.LinearOperatorHouseholder(reflection_axis)
with self.cached_session() as sess:
    sess.run([reflection_axis.initializer])
    self.check_convert_variables_to_tensors(operator)
