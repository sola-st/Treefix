# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
matrix_1 = array_ops.placeholder_with_default(rng.rand(4, 4), shape=None)
matrix_2 = array_ops.placeholder_with_default(rng.rand(3, 4), shape=None)
matrix_3 = array_ops.placeholder_with_default(rng.rand(3, 3), shape=None)
operators = [
    [linalg.LinearOperatorFullMatrix(matrix_1, is_square=True)],
    [linalg.LinearOperatorFullMatrix(matrix_2),
     linalg.LinearOperatorFullMatrix(matrix_3, is_square=True)]
]
operator = block_lower_triangular.LinearOperatorBlockLowerTriangular(
    operators)
x = np.random.rand(2, 4, 5).tolist()
msg = ("dimension does not match" if context.executing_eagerly()
       else "input structure is ambiguous")
with self.assertRaisesRegex(ValueError, msg):
    operator.matmul(x)
