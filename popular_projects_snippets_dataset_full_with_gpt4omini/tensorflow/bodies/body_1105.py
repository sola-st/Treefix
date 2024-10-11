# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
y, diags, rhs, expected_grad_diags, expected_grad_rhs = (
    self._makeDataForGradientWithBatching())

self._gradientTest(
    diags=diags,
    rhs=rhs,
    y=y,
    expected_grad_diags=expected_grad_diags,
    expected_grad_rhs=expected_grad_rhs)
