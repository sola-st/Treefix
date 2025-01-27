# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py

op_dimensions = [
    tensor_shape.Dimension(v) for v in op_dimension_values]
unknown_op_dimensions = [
    tensor_shape.Dimension(None) for _ in op_dimension_values]

batch_shape = [2, 1]
arg_dim = 5
if split_dim == -1:
    blockwise_arrays = [np.zeros(batch_shape + [arg_dim, d])
                        for d in op_dimension_values]
else:
    blockwise_arrays = [np.zeros(batch_shape + [d, arg_dim])
                        for d in op_dimension_values]

blockwise_list = [block.tolist() for block in blockwise_arrays]
blockwise_tensors = [ops.convert_to_tensor(block)
                     for block in blockwise_arrays]
blockwise_placeholders = [
    array_ops.placeholder_with_default(block, shape=None)
    for block in blockwise_arrays]

# Iterables of non-nested structures are always interpreted as blockwise.
# The list of lists is interpreted as blockwise as well, regardless of
# whether the operator dimensions are known, since the sizes of its elements
# along `split_dim` are non-identical.
for op_dims in [op_dimensions, unknown_op_dimensions]:
    for blockwise_inputs in [
        blockwise_arrays, blockwise_list,
        blockwise_tensors, blockwise_placeholders]:
        self.assertTrue(linear_operator_util.arg_is_blockwise(
            op_dims, blockwise_inputs, split_dim))
