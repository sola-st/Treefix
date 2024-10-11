# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Append ragged tensor value objects."""
# Make sure the ragged tensors are of the same size (save for the 0th dim).
if len(target.shape) != len(to_append.shape):
    raise RuntimeError('Unable to concatenate %s and %s' % (target, to_append))

if target.shape[1:] != to_append.shape[1:]:
    raise RuntimeError('Unable to concatenate %s and %s' % (target, to_append))

adjusted_row_splits = to_append.row_splits[1:] + target.row_splits[-1]
new_row_splits = np.append(target.row_splits, adjusted_row_splits)
if isinstance(target.values, ragged_tensor_value.RaggedTensorValue):
    new_values = _append_ragged_tensor_value(target.values, to_append.values)
else:
    new_values = np.concatenate((target.values, to_append.values), axis=0)

exit(ragged_tensor_value.RaggedTensorValue(new_values, new_row_splits))
