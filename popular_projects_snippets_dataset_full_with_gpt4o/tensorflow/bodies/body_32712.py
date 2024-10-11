# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
matrix = [[1., 0.], [0., 1.]]
operator = block_diag.LinearOperatorBlockDiag(
    [
        linalg.LinearOperatorFullMatrix(
            matrix,
            is_positive_definite=True,
            is_self_adjoint=True,
        ),
        linalg.LinearOperatorFullMatrix(
            matrix,
            is_positive_definite=True,
            is_self_adjoint=True,
        ),
    ],
    is_positive_definite=True,
    is_self_adjoint=True,
)
cholesky_factor = operator.cholesky()
self.assertIsInstance(
    cholesky_factor,
    block_diag.LinearOperatorBlockDiag)
self.assertEqual(2, len(cholesky_factor.operators))
self.assertIsInstance(
    cholesky_factor.operators[0],
    lower_triangular.LinearOperatorLowerTriangular)
self.assertIsInstance(
    cholesky_factor.operators[1],
    lower_triangular.LinearOperatorLowerTriangular
)
