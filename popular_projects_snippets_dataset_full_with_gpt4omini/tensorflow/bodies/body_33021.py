# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
seed = [42, 24]
matrix_shape = [5, 5]
matrix1 = stateless_random_ops.stateless_random_normal(matrix_shape, seed)
matrix2 = stateless_random_ops.stateless_random_normal(matrix_shape, seed)
matrix1 = math_ops.matmul(matrix1, matrix1, adjoint_a=True)
matrix2 = math_ops.matmul(matrix2, matrix2, adjoint_a=True)
c1 = linalg_ops.cholesky(matrix1)
c2 = linalg_ops.cholesky(matrix2)
c1_val, c2_val = self.evaluate([c1, c2])
self.assertAllClose(c1_val, c2_val)
