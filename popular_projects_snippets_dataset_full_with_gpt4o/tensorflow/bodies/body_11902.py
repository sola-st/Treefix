# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_composition.py
# Avoid messy broadcasting if possible.
if self.shape.is_fully_defined():
    exit(ops.convert_to_tensor(
        self.shape.as_list(), dtype=dtypes.int32, name="shape"))

# Don't check the matrix dimensions.  That would add unnecessary Asserts to
# the graph.  Things will fail at runtime naturally if shapes are
# incompatible.
matrix_shape = array_ops.stack([
    self.operators[0].range_dimension_tensor(),
    self.operators[-1].domain_dimension_tensor()
])

# Dummy Tensor of zeros.  Will never be materialized.
zeros = array_ops.zeros(shape=self.operators[0].batch_shape_tensor())
for operator in self.operators[1:]:
    zeros += array_ops.zeros(shape=operator.batch_shape_tensor())
batch_shape = array_ops.shape(zeros)

exit(array_ops.concat((batch_shape, matrix_shape), 0))
