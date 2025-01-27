# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_kronecker_test.py
matrix = [[1., 0.], [0., 1.]]
operator = kronecker.LinearOperatorKronecker(
    [
        linalg.LinearOperatorFullMatrix(
            matrix, is_non_singular=True),
        linalg.LinearOperatorFullMatrix(
            matrix, is_non_singular=True),
    ],
    is_non_singular=True,
)
inverse = operator.inverse()
self.assertIsInstance(
    inverse,
    kronecker.LinearOperatorKronecker)
self.assertEqual(2, len(inverse.operators))
