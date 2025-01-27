# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
diag = [1., 3., 5., 8.]
operator = linalg.LinearOperatorDiag(
    diag,
    is_positive_definite=True,
    is_self_adjoint=True,
)
self.assertIsInstance(operator.cholesky(), linalg.LinearOperatorDiag)
