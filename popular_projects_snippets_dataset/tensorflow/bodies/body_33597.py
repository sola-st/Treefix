# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
with self.session():
    matrix1 = random_ops.random_normal([5, 5], seed=42)
    matrix2 = random_ops.random_normal([5, 5], seed=42)
    det1 = linalg_ops.matrix_determinant(matrix1)
    det2 = linalg_ops.matrix_determinant(matrix2)
    det1_val, det2_val = self.evaluate([det1, det2])
    self.assertEqual(det1_val, det2_val)
