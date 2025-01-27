# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
self._test(
    diags=np.zeros(shape=(3, 0), dtype=np.float32),
    rhs=np.zeros(shape=(0, 1), dtype=np.float32),
    expected=np.zeros(shape=(0, 1), dtype=np.float32))
