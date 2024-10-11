# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._gradientTestWithLists(
    diags=_sample_diags,
    rhs=_sample_rhs,
    y=[1, 3, 2, 4],
    expected_grad_diags=[[-5, 0, 4, 0], [9, 0, -4, -16], [0, 0, 5, 16]],
    expected_grad_rhs=[1, 0, -1, 4])
