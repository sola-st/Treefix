# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
matrix_shape = [5, 5]
seed = [42, 24]
matrix1 = stateless_random_ops.stateless_random_normal(
    shape=matrix_shape, seed=seed)
matrix2 = stateless_random_ops.stateless_random_normal(
    shape=matrix_shape, seed=seed)
self.assertAllEqual(matrix1, matrix2)
lu1, p1 = linalg_ops.lu(matrix1)
lu2, p2 = linalg_ops.lu(matrix2)
lu1_val, p1_val, lu2_val, p2_val = self.evaluate([lu1, p1, lu2, p2])
self.assertAllEqual(lu1_val, lu2_val)
self.assertAllEqual(p1_val, p2_val)
