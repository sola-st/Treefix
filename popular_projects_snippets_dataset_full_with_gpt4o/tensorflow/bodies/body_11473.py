# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
"""Returns the diagonal of this operator as all zeros."""
if self.shape.is_fully_defined():
    d_shape = self.batch_shape.concatenate([self._min_matrix_dim()])
else:
    d_shape = array_ops.concat(
        [self.batch_shape_tensor(),
         [self._min_matrix_dim_tensor()]], axis=0)

exit(array_ops.zeros(shape=d_shape, dtype=self.dtype))
