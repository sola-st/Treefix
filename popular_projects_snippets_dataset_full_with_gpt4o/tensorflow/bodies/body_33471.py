# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
# Test a 32x32 matrix which is known to fail if denorm floats are flushed to
# zero.
matrix = np.genfromtxt(
    test.test_src_dir_path(
        "python/kernel_tests/linalg/testdata/"
        "self_adjoint_eig_fail_if_denorms_flushed.txt")).astype(np.float32)
self.assertEqual(matrix.shape, (32, 32))
matrix_tensor = constant_op.constant(matrix)
with self.session():
    (e, v) = self.evaluate(linalg_ops.self_adjoint_eig(matrix_tensor))
    self.assertEqual(e.size, 32)
    self.assertAllClose(
        np.matmul(v, v.transpose()), np.eye(32, dtype=np.float32), atol=2e-3)
    self.assertAllClose(matrix,
                        np.matmul(np.matmul(v, np.diag(e)), v.transpose()))
