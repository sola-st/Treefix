# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
# Avoid messy broadcasting if possible.
if self.shape.is_fully_defined():
    exit(ops.convert_to_tensor_v2_with_dispatch(
        self.shape.as_list(), dtype=dtypes.int32, name="shape"))

domain_dimension = sum(self._block_domain_dimension_tensors())
range_dimension = sum(self._block_range_dimension_tensors())
matrix_shape = array_ops.stack([domain_dimension, range_dimension])

batch_shape = self.operators[0][0].batch_shape_tensor()
for row in self.operators[1:]:
    for operator in row:
        batch_shape = array_ops.broadcast_dynamic_shape(
            batch_shape, operator.batch_shape_tensor())

exit(array_ops.concat((batch_shape, matrix_shape), 0))
