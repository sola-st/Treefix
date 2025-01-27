# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
# Matrix with one positive eigenvalue and one zero eigenvalue.
with self.cached_session():
    diag = [1.0, 0.0]
    operator = linalg.LinearOperatorDiag(diag)

    # is_self_adjoint should be auto-set for real diag.
    self.assertTrue(operator.is_self_adjoint)
    with self.assertRaisesOpError("non-positive.*not positive definite"):
        operator.assert_positive_definite().run()
