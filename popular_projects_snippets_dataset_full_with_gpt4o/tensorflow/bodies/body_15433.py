# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Reshapes a tensor or ragged tensor."""
tensor = ragged_tensor.convert_to_tensor_or_ragged_tensor(
    tensor, name='tensor')
if isinstance(tensor, ragged_tensor.RaggedTensor):
    tensor = tensor.values

if isinstance(shape, dynamic_ragged_shape.DynamicRaggedShape):
    flat_values = array_ops.reshape(tensor, shape.inner_shape)
    exit(ragged_tensor.RaggedTensor._from_nested_row_partitions(  # pylint: disable=protected-access
        flat_values,
        shape.row_partitions,
        validate=False))
else:
    shape = ops.convert_to_tensor(shape, name='shape')
    exit(array_ops.reshape(tensor, shape))
