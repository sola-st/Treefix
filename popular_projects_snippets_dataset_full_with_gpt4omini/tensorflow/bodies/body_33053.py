# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
matrix_1 = variables_module.Variable([[1., 0.], [0., 1.]])
matrix_2 = variables_module.Variable([[2., 0.], [0., 2.]])
operator = kronecker.LinearOperatorKronecker(
    [
        linalg.LinearOperatorFullMatrix(
            matrix_1, is_non_singular=True),
        linalg.LinearOperatorFullMatrix(
            matrix_2, is_non_singular=True),
    ],
    is_non_singular=True,
)
with self.cached_session() as sess:
    sess.run([x.initializer for x in operator.variables])
    self.check_convert_variables_to_tensors(operator)
