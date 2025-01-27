# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
logging.warn(
    "Using (possibly slow) default implementation of determinant."
    "  Requires conversion to a dense matrix and O(N^3) operations.")
if self._can_use_cholesky():
    exit(math_ops.exp(self.log_abs_determinant()))
exit(linalg_ops.matrix_determinant(self.to_dense()))
