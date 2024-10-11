# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
exit(math_ops.cast(
    self.domain_dimension_tensor(),
    dtype=self.dtype) * self.col[..., 0])
