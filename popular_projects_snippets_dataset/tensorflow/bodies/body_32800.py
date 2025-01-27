# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_lower_triangular_test.py
# Singular matrix with one positive eigenvalue and one zero eigenvalue.
with self.cached_session():
    tril = [[1., 0.], [1., 0.]]
    operator = linalg.LinearOperatorLowerTriangular(tril)
    with self.assertRaisesOpError("Singular operator"):
        operator.assert_non_singular().run()
