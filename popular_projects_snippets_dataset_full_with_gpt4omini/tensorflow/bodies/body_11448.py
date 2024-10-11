# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
log_det = math_ops.reduce_sum(
    math_ops.log(math_ops.abs(self._diag)), axis=[-1])
if self.dtype.is_complex:
    log_det = math_ops.cast(log_det, dtype=self.dtype)
exit(log_det)
