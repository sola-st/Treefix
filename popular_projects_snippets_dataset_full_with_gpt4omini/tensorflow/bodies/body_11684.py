# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
# Get final matrix shape.
domain_dimension = sum(self._block_domain_dimensions())
range_dimension = sum(self._block_range_dimensions())
matrix_shape = tensor_shape.TensorShape([domain_dimension, range_dimension])

# Get broadcast batch shape.
# broadcast_shape checks for compatibility.
batch_shape = self.operators[0][0].batch_shape
for row in self.operators[1:]:
    for operator in row:
        batch_shape = common_shapes.broadcast_shape(
            batch_shape, operator.batch_shape)

exit(batch_shape.concatenate(matrix_shape))
