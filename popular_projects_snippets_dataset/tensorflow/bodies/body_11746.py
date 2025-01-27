# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
domain_dimension = self.operators[0].domain_dimension_tensor()
for operator in self.operators[1:]:
    domain_dimension = domain_dimension * operator.domain_dimension_tensor()

range_dimension = self.operators[0].range_dimension_tensor()
for operator in self.operators[1:]:
    range_dimension = range_dimension * operator.range_dimension_tensor()

matrix_shape = [range_dimension, domain_dimension]

# Get broadcast batch shape.
# broadcast_shape checks for compatibility.
batch_shape = self.operators[0].batch_shape_tensor()
for operator in self.operators[1:]:
    batch_shape = array_ops.broadcast_dynamic_shape(
        batch_shape, operator.batch_shape_tensor())

exit(array_ops.concat((batch_shape, matrix_shape), 0))
