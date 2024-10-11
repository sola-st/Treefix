# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
matrix = [[0., 1.], [0., 1.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix, is_self_adjoint=True, is_positive_definite=True)
with self.cached_session():
    with self.assertRaisesOpError("not equal to its adjoint"):
        operator.assert_self_adjoint().run()
