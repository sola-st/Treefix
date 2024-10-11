# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
# The matrix and right-hand sides should have the same number of rows.
matrix = constant_op.constant([[1., 0.], [0., 1.]])
rhs = constant_op.constant([[1., 0.]])
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    self.evaluate(linalg_ops.matrix_solve(matrix, rhs))

# The matrix and right-hand side should have the same batch dimensions
matrix = np.random.normal(size=(2, 6, 2, 2))
rhs = np.random.normal(size=(2, 3, 2, 2))
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    self.evaluate(linalg_ops.matrix_solve(matrix, rhs))
