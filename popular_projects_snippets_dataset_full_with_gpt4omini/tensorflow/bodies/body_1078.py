# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=[[2.0, 0.0], [1.0, 3.0], [0.0, 1.0]],
    rhs=[1.0, 4.0],
    expected=[-5.0, 3.0])
