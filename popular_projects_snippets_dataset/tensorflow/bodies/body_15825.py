# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
shape_a = DynamicRaggedShape.from_lengths(
    lengths_a, num_row_partitions=num_row_partitions_a)
shape_b = DynamicRaggedShape.from_lengths(
    lengths_b, num_row_partitions=num_row_partitions_b)
rt_a = ragged_array_ops.ragged_reshape(
    _lowest_primes(_num_elements_of_lengths(lengths_a)), shape_a)
rt_b = ragged_array_ops.ragged_reshape(
    _lowest_primes(_num_elements_of_lengths(lengths_b)), shape_b)
if new_impl:
    result = dynamic_ragged_shape.ragged_binary_elementwise_op_impl(
        math_ops.add, rt_a, rt_b)
    shape_e = tensor_shape.TensorShape(shape_e)
    self.assertEqual(shape_e.as_list(), result.shape.as_list())
else:
    if isinstance(rt_a, RaggedTensor):
        rt_a = rt_a.with_row_splits_dtype(dtypes.int32)
    if isinstance(rt_b, RaggedTensor):
        rt_b = rt_b.with_row_splits_dtype(dtypes.int32)
    result = rt_a + rt_b
    shape_e = tensor_shape.TensorShape(shape_e)
    self.assertEqual(shape_e.as_list(), result.shape.as_list())
