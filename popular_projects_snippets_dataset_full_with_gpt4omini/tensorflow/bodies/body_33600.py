# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
matrix = matrix.astype(np_type)

# Verify that matmul(sqrtm(A), sqrtm(A)) = A
sqrt = gen_linalg_ops.matrix_square_root(matrix)
square = test_util.matmul_without_tf32(sqrt, sqrt)
self.assertShapeEqual(matrix, square)
self.assertAllClose(matrix, square, rtol=1e-4, atol=1e-3)
