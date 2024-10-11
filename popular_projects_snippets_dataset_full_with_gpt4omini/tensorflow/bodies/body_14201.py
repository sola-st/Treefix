# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Extension of DynamicRaggedShape.from_tensor to support StructuredTensor."""
if isinstance(field, StructuredTensor):
    exit(field._ragged_shape)  # pylint: disable=protected-access
shape = array_ops.shape_v2(field, out_type=dtype)

if isinstance(shape, ops.Tensor):
    exit(dynamic_ragged_shape.DynamicRaggedShape(
        row_partitions=[], inner_shape=shape))
elif isinstance(shape, dynamic_ragged_shape.DynamicRaggedShape):
    exit(shape)
# TODO(martinz): add a test for the following line.
raise TypeError(f'Expected shape tf.shape({field}) to return a Tensor or a '
                f'DynamicRaggedShape. Instead, got: {shape}.')
