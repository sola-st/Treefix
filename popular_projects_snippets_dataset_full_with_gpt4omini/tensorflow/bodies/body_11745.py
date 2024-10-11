# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
# Get final matrix shape.
domain_dimension = self.operators[0].domain_dimension
for operator in self.operators[1:]:
    domain_dimension = domain_dimension * operator.domain_dimension

range_dimension = self.operators[0].range_dimension
for operator in self.operators[1:]:
    range_dimension = range_dimension * operator.range_dimension

matrix_shape = tensor_shape.TensorShape([
    range_dimension, domain_dimension])

# Get broadcast batch shape.
# broadcast_shape checks for compatibility.
batch_shape = self.operators[0].batch_shape
for operator in self.operators[1:]:
    batch_shape = common_shapes.broadcast_shape(
        batch_shape, operator.batch_shape)

exit(batch_shape.concatenate(matrix_shape))
