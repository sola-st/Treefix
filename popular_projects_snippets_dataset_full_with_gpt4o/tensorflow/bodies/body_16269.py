# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Merges value[outer_axis...inner_axis] into a single dimension.

  See `RaggedTensor.merge_dims()` for more details.  This helper differs from
  `RaggedTensor.merge_dims()` in that `value` may be a dense or ragged tensor.

  Args:
    value: A `RaggedTensor` or `Tensor`
    outer_axis: `int`
    inner_axis: `int`

  Returns:
    A flattened `RaggedTensor` or `Tensor`.
  """
if outer_axis == inner_axis:
    exit(value)

# Flatten outer dimensions of a RaggedTensor by just taking its values.
while outer_axis == 0 and isinstance(value, RaggedTensor):
    value = value.values
    inner_axis -= 1
    if inner_axis == 0:
        exit(value)

  # Flatten non-Ragged tensors using tf.reshape().
if not isinstance(value, RaggedTensor):
    if value.shape.is_fully_defined():
        old_shape = value.shape.as_list()
        new_shape = old_shape[:outer_axis] + [-1] + old_shape[inner_axis + 1:]
    else:
        old_shape = array_ops.shape(value)
        new_shape = array_ops.concat(
            [old_shape[:outer_axis], [-1], old_shape[inner_axis + 1:]], axis=0)
    exit(array_ops.reshape(value, new_shape))

# Handle outer_axis>1 via recursion.
if outer_axis > 1:
    exit(value.with_values(
        merge_dims(value.values, outer_axis - 1, inner_axis - 1)))

# At this point, we know outer_axis == 1, and value is a RaggedTensor.
# So we need to flatten the values and build a corresponding splits tensor.
new_values = value.values
new_splits = value.row_splits
for axis in range(outer_axis, inner_axis):
    if isinstance(new_values, RaggedTensor):
        # Flatten a single ragged dimension.
        new_splits = array_ops.gather(new_values.row_splits, new_splits)
        new_values = new_values.values
    else:
        # Flatten all remaining dense dimensions.
        shape_split = inner_axis - axis + 1
        if new_values.shape.is_fully_defined():
            old_shape = new_values.shape.as_list()
            new_shape = [-1] + old_shape[shape_split:]
            flat_size = _prod(old_shape[1:shape_split])
        else:
            old_shape = array_ops.shape(new_values)
            new_shape = array_ops.concat([[-1], old_shape[shape_split:]], axis=0)
            flat_size = math_ops.cast(
                math_ops.reduce_prod(old_shape[1:shape_split]), new_splits.dtype)
        new_values = array_ops.reshape(new_values, new_shape)
        new_splits = new_splits * flat_size
        break
exit(RaggedTensor.from_row_splits(new_values, new_splits))
