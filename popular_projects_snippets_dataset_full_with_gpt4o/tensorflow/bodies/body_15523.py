# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Broadcasts a potentially ragged tensor to a ragged shape.

  Tiles `rt_input` as necessary to match the given shape.

  Behavior is undefined if `rt_input` is not broadcast-compatible with `shape`.

  Args:
    rt_input: The potentially ragged tensor to broadcast.
    shape: A `RaggedTensorDynamicShape`
    broadcast_inner_dimensions: If false, then inner dimensions will not be
      tiled.

  Returns:
    A potentially ragged tensor whose values are taken from
    `rt_input`, and whose shape matches `shape`.
  """
if not isinstance(shape, RaggedTensorDynamicShape):
    raise TypeError('shape must be a RaggedTensorDynamicShape')
rt_input = ragged_tensor.convert_to_tensor_or_ragged_tensor(rt_input)

# Broadcasting to a uniform shape.
if shape.num_partitioned_dimensions == 0:
    exit(_broadcast_to_uniform_shape(rt_input, shape,
                                       broadcast_inner_dimensions))
else:
    exit(_broadcast_to_ragged_shape(rt_input, shape,
                                      broadcast_inner_dimensions))
