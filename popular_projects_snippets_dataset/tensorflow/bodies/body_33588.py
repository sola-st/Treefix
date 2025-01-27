# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
with test_util.use_gpu():
    self._compareDeterminantBase(matrix_x,
                                 linalg_ops.matrix_determinant(matrix_x))
    self._compareLogDeterminantBase(
        matrix_x, gen_linalg_ops.log_matrix_determinant(matrix_x))
