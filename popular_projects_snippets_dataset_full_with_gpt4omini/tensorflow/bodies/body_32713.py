# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
matrix = [[1., 0.], [0., 1.]]
operator = block_diag.LinearOperatorBlockDiag(
    [
        linalg.LinearOperatorFullMatrix(
            matrix,
            is_non_singular=True,
        ),
        linalg.LinearOperatorFullMatrix(
            matrix,
            is_non_singular=True,
        ),
    ],
    is_non_singular=True,
)
inverse = operator.inverse()
self.assertIsInstance(
    inverse,
    block_diag.LinearOperatorBlockDiag)
self.assertEqual(2, len(inverse.operators))
