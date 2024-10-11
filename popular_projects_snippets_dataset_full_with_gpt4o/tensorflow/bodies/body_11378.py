# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
# Get Tensor of all ones of same shape as self.batch_shape.
if self.batch_shape.is_fully_defined():
    batch_of_ones = array_ops.ones(shape=self.batch_shape, dtype=self.dtype)
else:
    batch_of_ones = array_ops.ones(
        shape=self.batch_shape_tensor(), dtype=self.dtype)

if self._min_matrix_dim() is not None:
    exit(self.multiplier * self._min_matrix_dim() * batch_of_ones)
else:
    exit((self.multiplier * math_ops.cast(self._min_matrix_dim_tensor(),
                                            self.dtype) * batch_of_ones))
