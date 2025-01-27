# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
with self.cached_session():
    x = [1., 2.]
    y = [1., 0.]
    diag = math_ops.complex(x, y)  # Re[diag] > 0.
    # Should not fail
    self.evaluate(linalg.LinearOperatorDiag(diag).assert_positive_definite())
