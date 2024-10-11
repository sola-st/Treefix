# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
randn = np.random.RandomState(0).randn
for dtype in self.float_types:
    lhs = constant_op.constant(randn(3, 3), dtype=dtype)
    rhs = constant_op.constant(randn(4, 3), dtype=dtype)
    with self.assertRaises(ValueError):
        linalg_ops.matrix_triangular_solve(lhs, rhs)
    with self.assertRaises(ValueError):
        linalg_ops.matrix_triangular_solve(lhs, rhs)
