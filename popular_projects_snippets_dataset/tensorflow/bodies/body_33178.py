# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
matrix = [[1., 1.], [1., 1.]]
operator = linalg.LinearOperatorFullMatrix(matrix, is_self_adjoint=True)
with self.cached_session():
    with self.assertRaises(errors.InvalidArgumentError):
        operator.assert_positive_definite().run()
