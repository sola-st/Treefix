# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=[[2.0, -1.0, 0.0], [1.0, 3.0, 1.0], [0.0, -1.0, -2.0]],
    rhs=[1.0, 2.0, 3.0],
    expected=[-3.0, 2.0, 7.0])
