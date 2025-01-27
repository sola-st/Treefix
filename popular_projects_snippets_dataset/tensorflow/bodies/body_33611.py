# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
matrix_shape = [5, 5]
seed = [42, 24]
matrix1 = stateless_random_ops.stateless_random_normal(
    shape=matrix_shape, seed=seed)
matrix2 = stateless_random_ops.stateless_random_normal(
    shape=matrix_shape, seed=seed)
self.assertAllEqual(matrix1, matrix2)
square1 = math_ops.matmul(matrix1, matrix1)
square2 = math_ops.matmul(matrix2, matrix2)
sqrt1 = gen_linalg_ops.matrix_square_root(square1)
sqrt2 = gen_linalg_ops.matrix_square_root(square2)
all_ops = [sqrt1, sqrt2]
sqrt = self.evaluate(all_ops)
self.assertAllClose(sqrt[0], sqrt[1])
