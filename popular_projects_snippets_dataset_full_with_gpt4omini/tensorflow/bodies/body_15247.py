# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Broadcasts a potentially ragged tensor to a ragged shape.

  Tiles `rt_input` as necessary to match the given shape.

  Behavior is undefined if `rt_input` is not broadcast-compatible with `shape`.

  Args:
    rt_input: The potentially ragged tensor to broadcast.
    shape: A `DynamicRaggedShape`

  Returns:
    A potentially ragged tensor whose values are taken from
    `rt_input`, and whose shape matches `shape`.
  """
if not isinstance(shape, DynamicRaggedShape):
    raise TypeError("shape must be a DynamicRaggedShape")
rt_input = ragged_tensor.convert_to_tensor_or_ragged_tensor(rt_input)
origin_shape = None
if ragged_tensor.is_ragged(rt_input):
    if shape.num_row_partitions != 0:
        if rt_input.row_splits.dtype != shape.dtype:
            raise ValueError("Cannot coerce row_splits.dtype")
    else:
        shape = shape.with_dtype(rt_input.row_splits.dtype)
    origin_shape = DynamicRaggedShape.from_tensor(rt_input)
else:
    if shape.num_row_partitions != 0:
        origin_shape = DynamicRaggedShape.from_tensor(rt_input, dtype=shape.dtype)
    else:
        origin_shape = DynamicRaggedShape.from_tensor(
            rt_input, dtype=dtypes.int64)
        shape = shape.with_dtype(dtype=dtypes.int64)

broadcaster = _get_broadcaster(origin_shape, shape)
exit(broadcaster.broadcast(rt_input))
