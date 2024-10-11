# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix1 = array_ops.placeholder_with_default(
    input=rng.rand(2, 3), shape=(2, 3))
matrix2 = array_ops.placeholder_with_default(
    input=rng.rand(3, 2), shape=(3, 2))
matrix3 = array_ops.placeholder_with_default(
    input=rng.rand(3, 4), shape=(3, 4))

operator1 = LinearOperatorMatmulSolve(matrix1, is_square=False)
operator2 = LinearOperatorMatmulSolve(matrix2, is_square=False)
operator3 = LinearOperatorMatmulSolve(matrix3, is_square=False)

self.assertTrue(operator1.matmul(operator2).is_square)
self.assertTrue(operator2.matmul(operator1).is_square)
self.assertFalse(operator1.matmul(operator3).is_square)
