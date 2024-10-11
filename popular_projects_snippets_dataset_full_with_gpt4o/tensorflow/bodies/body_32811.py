# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
seed = [42, 24]
all_ops = []
for full_matrices_ in True, False:
    for rows_ in 4, 5:
        for cols_ in 4, 5:
            matrix_shape = [rows_, cols_]
            matrix1 = stateless_random_ops.stateless_random_normal(
                matrix_shape, seed)
            matrix2 = stateless_random_ops.stateless_random_normal(
                matrix_shape, seed)
            self.assertAllEqual(matrix1, matrix2)
            q1, r1 = linalg_ops.qr(matrix1, full_matrices=full_matrices_)
            q2, r2 = linalg_ops.qr(matrix2, full_matrices=full_matrices_)
            all_ops += [q1, q2, r1, r2]
val = self.evaluate(all_ops)
for i in range(0, len(val), 2):
    self.assertAllClose(val[i], val[i + 1])
