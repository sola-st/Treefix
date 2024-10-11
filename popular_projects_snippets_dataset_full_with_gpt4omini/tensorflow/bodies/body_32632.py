# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
with self.session() as sess:
    all_ops = []
    for adjoint_ in True, False:
        matrix1 = random_ops.random_normal([5, 5], seed=42)
        matrix2 = random_ops.random_normal([5, 5], seed=42)
        inv1 = linalg_ops.matrix_inverse(matrix1, adjoint=adjoint_)
        inv2 = linalg_ops.matrix_inverse(matrix2, adjoint=adjoint_)
        all_ops += [inv1, inv2]
    inv = self.evaluate(all_ops)
    self.assertAllEqual(inv[0], inv[1])
    self.assertAllEqual(inv[2], inv[3])
