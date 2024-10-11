# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
if self.batch_shape.is_fully_defined():
    exit(array_ops.zeros(shape=self.batch_shape, dtype=self.dtype))
else:
    exit(array_ops.zeros(shape=self.batch_shape_tensor(), dtype=self.dtype))
