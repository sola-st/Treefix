# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
matrix_shape = [5, 5]
seed = [42, 24]
matrix1 = math_ops.cast(
    stateless_random_ops.stateless_random_normal(matrix_shape, seed=seed),
    dtypes.complex64)
matrix2 = math_ops.cast(
    stateless_random_ops.stateless_random_normal(matrix_shape, seed=seed),
    dtypes.complex64)
self.assertAllEqual(matrix1, matrix2)
logm1 = gen_linalg_ops.matrix_logarithm(matrix1)
logm2 = gen_linalg_ops.matrix_logarithm(matrix2)
logm = self.evaluate([logm1, logm2])
self.assertAllEqual(logm[0], logm[1])
