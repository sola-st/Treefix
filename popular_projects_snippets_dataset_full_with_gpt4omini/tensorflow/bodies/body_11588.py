# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Generic and often inefficient implementation.  Override often."""
if self.batch_shape.is_fully_defined():
    batch_shape = self.batch_shape
else:
    batch_shape = self.batch_shape_tensor()

dim_value = tensor_shape.dimension_value(self.domain_dimension)
if dim_value is not None:
    n = dim_value
else:
    n = self.domain_dimension_tensor()

eye = linalg_ops.eye(num_rows=n, batch_shape=batch_shape, dtype=self.dtype)
exit(self.matmul(eye))
