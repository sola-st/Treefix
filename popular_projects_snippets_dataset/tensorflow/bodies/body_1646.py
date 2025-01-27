# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
rng = np.random.RandomState(0)
shapes = [((4, 3, 3), (4, 3, 5)), ((1, 2, 2), (1, 2, 1)),
          ((1, 1, 1), (1, 1, 2)), ((2, 3, 4, 4), (2, 3, 4, 1))]
tuples = itertools.product(self.float_types, shapes)
for dtype, (a_shape, b_shape) in tuples:
    n = a_shape[-1]
    a = np.tril(rng.rand(*a_shape) - 0.5) / (2.0 * n) + np.eye(n)
    b = rng.randn(*b_shape)
    self._VerifyTriangularSolveCombo(
        a.astype(dtype), b.astype(dtype), atol=1e-3)
