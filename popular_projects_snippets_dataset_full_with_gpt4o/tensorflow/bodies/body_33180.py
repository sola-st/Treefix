# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
matrix = variables_module.Variable([[3.]])
operator = linalg.LinearOperatorFullMatrix(matrix)
with self.cached_session() as sess:
    sess.run([matrix.initializer])
    self.check_convert_variables_to_tensors(operator)
