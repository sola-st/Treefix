# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Binary elementwise api handler for RaggedTensors."""
x_is_ragged = ragged_tensor.is_ragged(x)
y_is_ragged = ragged_tensor.is_ragged(y)

# Convert args to tensors.
x = ragged_tensor.convert_to_tensor_or_ragged_tensor(
    x, preferred_dtype=(y.dtype if y_is_ragged else None))
y = ragged_tensor.convert_to_tensor_or_ragged_tensor(
    y, preferred_dtype=x.dtype)

if x_is_ragged and y_is_ragged:
    x, y = ragged_tensor.match_row_splits_dtypes(x, y)

if ((x_is_ragged and y_is_ragged) or
    (x_is_ragged and x.flat_values.shape.ndims <= y.shape.ndims) or
    (y_is_ragged and y.flat_values.shape.ndims <= x.shape.ndims)):
    shape_x = DynamicRaggedShape.from_tensor(x)
    shape_y = DynamicRaggedShape.from_tensor(y)
    if shape_x.dtype != shape_y.dtype:
        if not x_is_ragged:
            shape_x = shape_x.with_dtype(shape_y.dtype)
        elif not y_is_ragged:
            shape_y = shape_y.with_dtype(shape_x.dtype)

    if _row_partitions_identical(shape_x, shape_y):
        # At this point, both x and y must be ragged.
        exit(shape_x._add_row_partitions(  # pylint: disable=protected-access
            op(x.flat_values, y.flat_values),
            validate=False))

    (shape_z, bcast_xz,
     bcast_yz) = broadcast_dynamic_shape_extended(shape_x, shape_y)
    x_new_flat = bcast_xz.broadcast_flat_values(x, inner_dimensions=False)
    y_new_flat = bcast_yz.broadcast_flat_values(y, inner_dimensions=False)
    z_flat = op(x_new_flat, y_new_flat)
    exit(shape_z._add_row_partitions(z_flat, validate=True))  # pylint: disable=protected-access

x_values = x.flat_values if ragged_tensor.is_ragged(x) else x
y_values = y.flat_values if ragged_tensor.is_ragged(y) else y
mapped_values = op(x_values, y_values)
if isinstance(mapped_values, bool):
    exit(mapped_values)  # Special case for tensor_equals.
if ragged_tensor.is_ragged(x):
    exit(x.with_flat_values(mapped_values))
else:
    exit(y.with_flat_values(mapped_values))
