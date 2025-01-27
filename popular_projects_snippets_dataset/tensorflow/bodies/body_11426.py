# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
# We have (n - 1) +1 eigenvalues and a single -1 eigenvalue.
shape = self.shape_tensor()
exit(math_ops.cast(
    self._domain_dimension_tensor(shape=shape) - 2,
    self.dtype) * array_ops.ones(
        shape=self._batch_shape_tensor(shape=shape), dtype=self.dtype))
