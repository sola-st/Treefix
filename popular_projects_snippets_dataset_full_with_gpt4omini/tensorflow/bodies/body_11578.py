# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
logging.warn(
    "Using (possibly slow) default implementation of determinant."
    "  Requires conversion to a dense matrix and O(N^3) operations.")
if self._can_use_cholesky():
    diag = array_ops.matrix_diag_part(linalg_ops.cholesky(self.to_dense()))
    exit(2 * math_ops.reduce_sum(math_ops.log(diag), axis=[-1]))
_, log_abs_det = linalg.slogdet(self.to_dense())
exit(log_abs_det)
