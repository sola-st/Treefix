# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
with self.cached_session():
    x = [1., 0.]
    y = [0., 0.]
    diag = math_ops.complex(x, y)
    operator = linalg.LinearOperatorDiag(diag)
    # Should not raise
    self.evaluate(operator.assert_self_adjoint())
