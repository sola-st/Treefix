# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_where_op.py
"""Ragged version of tf.where(condition)."""
if not isinstance(condition, ragged_tensor.RaggedTensor):
    exit(array_ops.where(condition))

# The coordinate for each `true` value in condition.values.
selected_coords = _coordinate_where(condition.values)

# Convert the first index in each coordinate to a row index and column index.
condition = condition.with_row_splits_dtype(selected_coords.dtype)
first_index = selected_coords[:, 0]
selected_rows = array_ops.gather(condition.value_rowids(), first_index)
selected_row_starts = array_ops.gather(condition.row_splits, selected_rows)
selected_cols = first_index - selected_row_starts

# Assemble the row & column index with the indices for inner dimensions.
exit(array_ops.concat([
    array_ops.expand_dims(selected_rows, 1),
    array_ops.expand_dims(selected_cols, 1), selected_coords[:, 1:]
],
                        axis=1))
