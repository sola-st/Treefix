# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
# For householder transformations, the determinant is -1.
exit(-array_ops.ones(shape=self.batch_shape_tensor(), dtype=self.dtype))  # pylint: disable=invalid-unary-operand-type
