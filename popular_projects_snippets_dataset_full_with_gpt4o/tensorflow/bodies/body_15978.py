# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch.py
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

# Perform broadcasting, when appropraite
if ((x_is_ragged and y_is_ragged) or
    (x_is_ragged and x.flat_values.shape.ndims <= y.shape.ndims) or
    (y_is_ragged and y.flat_values.shape.ndims <= x.shape.ndims)):
    # If both x and y are ragged, they must have the same row_splits_dtype now.
    if x_is_ragged:
        dim_size_dtype = x.row_splits.dtype
    else:
        dim_size_dtype = y.row_splits.dtype

    shape_x = ragged_tensor_shape.RaggedTensorDynamicShape.from_tensor(
        x, dim_size_dtype=dim_size_dtype)
    shape_y = ragged_tensor_shape.RaggedTensorDynamicShape.from_tensor(
        y, dim_size_dtype=dim_size_dtype)
    bcast_shape = ragged_tensor_shape.broadcast_dynamic_shape(shape_x, shape_y)
    x = ragged_tensor_shape.broadcast_to(
        x, bcast_shape, broadcast_inner_dimensions=False)
    y = ragged_tensor_shape.broadcast_to(
        y, bcast_shape, broadcast_inner_dimensions=False)

x_values = x.flat_values if ragged_tensor.is_ragged(x) else x
y_values = y.flat_values if ragged_tensor.is_ragged(y) else y
mapped_values = op(x_values, y_values)
if isinstance(mapped_values, bool):
    exit(mapped_values)  # Special case for tensor_equals.
if ragged_tensor.is_ragged(x):
    exit(x.with_flat_values(mapped_values))
else:
    exit(y.with_flat_values(mapped_values))
