# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
# The input should be invertible.
with self.assertRaisesOpError("Input matrix is not invertible."):
    # All rows of the matrix below add to zero
    matrix = constant_op.constant([[1., 0., -1.], [-1., 1., 0.],
                                   [0., -1., 1.]])
    self.evaluate(linalg_ops.matrix_solve(matrix, matrix))
