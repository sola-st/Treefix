# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Returns the shape formed by broadcasting two shapes to be compatible.

  Args:
    shape_x: A `RaggedTensorDynamicShape`
    shape_y: A `RaggedTensorDynamicShape`

  Returns:
    A `RaggedTensorDynamicShape`.
  Raises:
    ValueError: If `shape_x` and `shape_y` are not broadcast-compatible.
  """
if not isinstance(shape_x, RaggedTensorDynamicShape):
    raise TypeError('shape_x must be a RaggedTensorDynamicShape')
if not isinstance(shape_y, RaggedTensorDynamicShape):
    raise TypeError('shape_y must be a RaggedTensorDynamicShape')

# Broadcast both shapes to have the same rank.
if shape_x.rank is None or shape_y.rank is None:
    raise ValueError('Unable to broadcast: unknown rank')
broadcast_rank = max(shape_x.rank, shape_y.rank)
shape_x = shape_x.broadcast_to_rank(broadcast_rank)
shape_y = shape_y.broadcast_to_rank(broadcast_rank)

# Broadcast dimensions one at a time, starting from the outermost dimension.
for axis in range(broadcast_rank):
    shape_x = shape_x.broadcast_dimension(axis, shape_y.dimension_size(axis))
    shape_y = shape_y.broadcast_dimension(axis, shape_x.dimension_size(axis))

exit(shape_x)
