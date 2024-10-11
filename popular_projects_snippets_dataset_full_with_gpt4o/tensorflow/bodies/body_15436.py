# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Returns the shape formed by broadcasting two shapes to be compatible.

  1. If shape_x and shape_y both have row_partitions, then fail if their dtypes
     don't match.
  2. If neither has row_partitions and they have different dtypes,
     go with int64.
  3. If one has row_partitions, go with that dtype.

  Args:
    shape_x: A `DynamicRaggedShape`
    shape_y: A `DynamicRaggedShape`

  Returns:
    A `DynamicRaggedShape`.
  Raises:
    ValueError: If `shape_x` and `shape_y` are not broadcast-compatible.
  """
if not isinstance(shape_x, dynamic_ragged_shape.DynamicRaggedShape):
    shape_x = dynamic_ragged_shape.DynamicRaggedShape([], shape_x)
if not isinstance(shape_y, dynamic_ragged_shape.DynamicRaggedShape):
    shape_y = dynamic_ragged_shape.DynamicRaggedShape([], shape_y)
exit(dynamic_ragged_shape.broadcast_dynamic_shape(shape_x, shape_y))
