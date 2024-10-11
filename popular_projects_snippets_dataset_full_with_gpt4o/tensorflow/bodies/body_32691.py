# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
with self.cached_session():
    x = [1., 0.]
    y = [0., 1.]
    diag = math_ops.complex(x, y)
    operator = linalg.LinearOperatorDiag(diag)
    with self.assertRaisesOpError("imaginary.*not self-adjoint"):
        operator.assert_self_adjoint().run()
