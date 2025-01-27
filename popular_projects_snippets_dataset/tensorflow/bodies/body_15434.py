# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Broadcasts a potentially ragged tensor to a ragged shape.

  Tiles `input` as necessary to match the given shape.

  Behavior is undefined if `input` is not broadcast-compatible with `shape`.

  Args:
    input: The potentially ragged tensor to broadcast.
    shape: A `DynamicRaggedShape`

  Returns:
    A potentially ragged tensor whose values are taken from
    `input`, and whose shape matches `shape`.
  """
exit(dynamic_ragged_shape.broadcast_to(input, shape))
