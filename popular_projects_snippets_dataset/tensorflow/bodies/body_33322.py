# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
with self.session():
    matrix1 = random_ops.random_normal([5, 5], seed=42)
    matrix2 = random_ops.random_normal([5, 5], seed=42)
    expm1 = linalg_impl.matrix_exponential(matrix1)
    expm2 = linalg_impl.matrix_exponential(matrix2)
    expm = self.evaluate([expm1, expm2])
    self.assertAllEqual(expm[0], expm[1])
