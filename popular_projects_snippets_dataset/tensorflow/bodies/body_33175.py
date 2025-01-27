# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
with self.cached_session():
    tril = linear_operator_test_util.random_tril_matrix(
        shape=(50, 50), dtype=np.float32)
    diag = np.logspace(-2, 2, 50).astype(np.float32)
    tril = array_ops.matrix_set_diag(tril, diag)
    matrix = self.evaluate(math_ops.matmul(tril, tril, transpose_b=True))
    operator = linalg.LinearOperatorFullMatrix(matrix)
    with self.assertRaisesOpError("Singular matrix"):
        # Ensure that we have finite condition number...just HUGE.
        cond = np.linalg.cond(matrix)
        self.assertTrue(np.isfinite(cond))
        self.assertGreater(cond, 1e12)
        operator.assert_non_singular().run()
