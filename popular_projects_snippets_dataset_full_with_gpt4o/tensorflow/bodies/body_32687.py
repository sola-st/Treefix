# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
with self.cached_session():
    diag_x = [1.0, -2.0]
    diag_y = [0., 0.]  # Imaginary eigenvalues should not matter.
    diag = math_ops.complex(diag_x, diag_y)
    operator = linalg.LinearOperatorDiag(diag)

    # is_self_adjoint should not be auto-set for complex diag.
    self.assertTrue(operator.is_self_adjoint is None)
    with self.assertRaisesOpError("non-positive real.*not positive definite"):
        operator.assert_positive_definite().run()
