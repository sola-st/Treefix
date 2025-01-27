# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
diag_entry = self.col[..., 0:1]
exit(diag_entry * array_ops.ones(
    [self.domain_dimension_tensor()], self.dtype))
