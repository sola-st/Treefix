# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
# The matrix and right-hand sides should have the same number of rows.
with self.session():
    matrix = constant_op.constant([[1., 0.], [0., 1.]])
    rhs = constant_op.constant([[1., 0.]])
    with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
        linalg_ops.matrix_solve_ls(matrix, rhs)
