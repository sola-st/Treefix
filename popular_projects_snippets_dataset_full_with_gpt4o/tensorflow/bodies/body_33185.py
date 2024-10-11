# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
matrix = [[1., 1.], [1., 1.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix, is_self_adjoint=True, is_positive_definite=True)
with self.cached_session():
    # Cholesky decomposition may fail, so the error is not specific to
    # non-singular.
    with self.assertRaisesOpError(""):
        operator.assert_non_singular().run()
