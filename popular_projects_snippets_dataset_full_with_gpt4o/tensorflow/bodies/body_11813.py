# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
exit(check_ops.assert_equal(
    self.row,
    self.col,
    message=("row and col are not the same, and "
             "so this operator is not self-adjoint.")))
