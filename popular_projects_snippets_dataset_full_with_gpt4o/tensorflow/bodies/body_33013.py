# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
chol_np, verification_np = self.evaluate([chol, verification])
self.assertAllClose(x, verification_np)
self.assertShapeEqual(x, chol)
# Check that the cholesky is lower triangular, and has positive diagonal
# elements.
if chol_np.shape[-1] > 0:
    chol_reshaped = np.reshape(chol_np, (-1, chol_np.shape[-2],
                                         chol_np.shape[-1]))
    for chol_matrix in chol_reshaped:
        self.assertAllClose(chol_matrix, np.tril(chol_matrix))
        self.assertTrue((np.diag(chol_matrix) > 0.0).all())
