# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
y, diags, rhs, expected_grad_diags, expected_grad_rhs = \
      self._makeDataForGradientWithBatching()

self._gradientTestWithLists(
    diags=diags,
    rhs=rhs,
    y=y,
    expected_grad_diags=expected_grad_diags,
    expected_grad_rhs=expected_grad_rhs)
