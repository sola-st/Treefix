# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
n = 1024
rng = np.random.RandomState(0)
a = np.tril(rng.rand(n, n) - 0.5) / (2.0 * n) + np.eye(n)
b = rng.randn(n, n)
self._VerifyTriangularSolve(
    a.astype(np.float32), b.astype(np.float32), True, False, 1e-4)
