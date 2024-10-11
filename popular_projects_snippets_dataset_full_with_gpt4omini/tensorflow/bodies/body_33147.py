# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._gradientTestWithLists(
    diags=_sample_diags,
    rhs=[[1, 2], [2, 4], [3, 6], [4, 8]],
    y=[[1, 5], [2, 6], [3, 7], [4, 8]],
    expected_grad_diags=([[-20, 28, -60, 0], [36, -35, 60, 80],
                          [0, 63, -75, -80]]),
    expected_grad_rhs=[[0, 2], [1, 3], [1, 7], [0, -10]])
