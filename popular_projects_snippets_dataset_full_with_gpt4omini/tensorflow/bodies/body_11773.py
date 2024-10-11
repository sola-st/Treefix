# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
# Get final matrix shape.
domain_dimension = sum(self._block_domain_dimensions())
range_dimension = sum(self._block_range_dimensions())
matrix_shape = tensor_shape.TensorShape([range_dimension, domain_dimension])

# Get broadcast batch shape.
# broadcast_shape checks for compatibility.
batch_shape = self.operators[0].batch_shape
for operator in self.operators[1:]:
    batch_shape = common_shapes.broadcast_shape(
        batch_shape, operator.batch_shape)

exit(batch_shape.concatenate(matrix_shape))
