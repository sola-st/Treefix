# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_lower_triangular_test.py
# The tril matrix here is selected so that multiplying the rows by the sign
# (the correct thing to do) is different than multiplying the columns.
l = linalg_lib.LinearOperatorLowerTriangular(
    [[-1., 0., 0.], [0.5, 0.2, 0.], [0.1, 0.1, 1.]], is_non_singular=True)
llt = l @ l.H
chol = llt.cholesky()
self.assertIsInstance(chol, linalg_lib.LinearOperatorLowerTriangular)
self.assertGreater(self.evaluate(chol.diag_part()).min(), 0)
self.assertAllClose(
    self.evaluate(llt.to_dense()), self.evaluate(
        (chol @ chol.H).to_dense()))
