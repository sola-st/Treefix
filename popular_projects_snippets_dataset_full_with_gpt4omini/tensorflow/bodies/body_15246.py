# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
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
if not isinstance(shape_x, DynamicRaggedShape):
    raise TypeError("shape_x must be a DynamicRaggedShape")
if not isinstance(shape_y, DynamicRaggedShape):
    raise TypeError("shape_y must be a DynamicRaggedShape")

exit(broadcast_dynamic_shape_extended(shape_x, shape_y)[0])
