# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
matrix = [[1., 0.], [0., 1.]]
operator = block_lower_triangular.LinearOperatorBlockLowerTriangular(
    [[linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)],
     [linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True),
      linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)]],
    is_non_singular=True,
)
inverse = operator.inverse()
self.assertIsInstance(
    inverse,
    block_lower_triangular.LinearOperatorBlockLowerTriangular)
self.assertEqual(2, len(inverse.operators))
self.assertEqual(1, len(inverse.operators[0]))
self.assertEqual(2, len(inverse.operators[1]))
