# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
rng = np.random.RandomState(0)
a = np.tril(rng.randn(5, 5))
b = rng.randn(5, 7)
self._VerifyTriangularSolveCombo(a, b, atol=5e-2, dtype=dtypes.bfloat16)
