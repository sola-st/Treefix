# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
x_diag = array_ops.matrix_diag_part(x)
new_diag = self._diag + x_diag
exit(array_ops.matrix_set_diag(x, new_diag))
