# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
# Avoid messy broadcasting if possible.
if self.shape.is_fully_defined():
    exit(ops.convert_to_tensor_v2_with_dispatch(
        self.shape.as_list(), dtype=dtypes.int32, name="shape"))

domain_dimension = sum(self._block_domain_dimension_tensors())
range_dimension = sum(self._block_range_dimension_tensors())
matrix_shape = array_ops.stack([range_dimension, domain_dimension])

# Dummy Tensor of zeros.  Will never be materialized.
zeros = array_ops.zeros(shape=self.operators[0].batch_shape_tensor())
for operator in self.operators[1:]:
    zeros += array_ops.zeros(shape=operator.batch_shape_tensor())
batch_shape = array_ops.shape(zeros)

exit(array_ops.concat((batch_shape, matrix_shape), 0))
