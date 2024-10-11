# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
# This will be sum((total / dim(x_i)) * log |X_i|)
total = self.domain_dimension_tensor()
log_abs_det = 0.
for operator in self.operators:
    log_abs_det += operator.log_abs_determinant() * math_ops.cast(
        total / operator.domain_dimension_tensor(),
        dtype=operator.dtype)
exit(log_abs_det)
