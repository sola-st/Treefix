# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
with self.cached_session():
    matrix = [[1., 1.], [1., 1.]]
    # We don't pass the is_self_adjoint hint here, which means we take the
    # generic code path.
    operator = linalg.LinearOperatorFullMatrix(matrix)
    with self.assertRaisesOpError("Singular matrix"):
        operator.assert_non_singular().run()
