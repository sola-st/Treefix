# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
rng = np.random.RandomState(0)
for dtype in self.float_types:
    a = rng.randn(3, 4).astype(dtype)
    b = rng.randn(4, 4).astype(dtype)
    with self.test_scope():
        with self.assertRaises((ValueError, errors.InvalidArgumentError)):
            linalg_ops.matrix_triangular_solve(a, b)
