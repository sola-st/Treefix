# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
if self.diagonals_format == _MATRIX:
    exit(array_ops.matrix_diag_part(self.diagonals))
elif self.diagonals_format == _SEQUENCE:
    diagonal = self.diagonals[1]
    exit(array_ops.broadcast_to(
        diagonal, self.shape_tensor()[:-1]))
else:
    exit(self.diagonals[..., 1, :])
