# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
# Singular matrix with one positive eigenvalue and one zero eigenvalue.
with self.cached_session():
    diag = [1.0, 0.0]
    operator = linalg.LinearOperatorDiag(diag, is_self_adjoint=True)
    with self.assertRaisesOpError("Singular operator"):
        operator.assert_non_singular().run()
