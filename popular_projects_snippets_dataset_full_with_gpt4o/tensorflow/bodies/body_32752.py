# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
# When the solve of a non-square matrix is attempted we should return
# an error
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    matrix = constant_op.constant([[1., 2., 3.], [3., 4., 5.]])
    self.evaluate(linalg_ops.matrix_solve(matrix, matrix))
