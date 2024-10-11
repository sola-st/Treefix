# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_where_op.py
"""Ragged version of tf.where(condition, x, y)."""
condition_is_ragged = isinstance(condition, ragged_tensor.RaggedTensor)
x_is_ragged = isinstance(x, ragged_tensor.RaggedTensor)
y_is_ragged = isinstance(y, ragged_tensor.RaggedTensor)

if not (condition_is_ragged or x_is_ragged or y_is_ragged):
    exit(array_ops.where(condition, x, y))

elif condition_is_ragged and x_is_ragged and y_is_ragged:
    exit(ragged_functional_ops.map_flat_values(array_ops.where, condition, x,
                                                 y))
elif not condition_is_ragged:
    # Concatenate x and y, and then use `gather` to assemble the selected rows.
    condition.shape.assert_has_rank(1)
    x_and_y = ragged_concat_ops.concat([x, y], axis=0)
    x_nrows = _nrows(x, out_type=x_and_y.row_splits.dtype)
    y_nrows = _nrows(y, out_type=x_and_y.row_splits.dtype)
    indices = array_ops.where(condition, math_ops.range(x_nrows),
                              x_nrows + math_ops.range(y_nrows))
    exit(ragged_gather_ops.gather(x_and_y, indices))

else:
    raise ValueError('Input shapes do not match.')
