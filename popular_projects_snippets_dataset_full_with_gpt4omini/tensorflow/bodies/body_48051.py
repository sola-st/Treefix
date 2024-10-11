# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Append sparse tensor value objects."""
# Make sure the sparse tensors are of the same size (except for the 0th dim).
if len(target.dense_shape) != len(to_append.dense_shape):
    raise RuntimeError(
        'Unable to concatenate %s and %s. The inner dense shapes do not '
        'have the same number of dimensions (%s vs %s)' %
        (target, to_append, target.dense_shape, to_append.dense_shape))

if target.dense_shape[1:] != to_append.dense_shape[1:]:
    raise RuntimeError(
        'Unable to concatenate %s and %s. The inner dense shapes do not '
        'match inner dimensions (%s vs %s)' %
        (target, to_append, target.dense_shape[1:], to_append.dense_shape[1:]))

# Add the to_append indices to target, updating the 0th value, and keeping
# track of the maximum so we know the final dense_shape of this tensor.
base_dim0_value = target.dense_shape[0]
max_dim0_value = target.dense_shape[0]
new_indices = target.indices
for index in to_append.indices:
    # Here, we iterate through the sparse indices of the tensor to append. For
    # each index, we update its zeroth value (the batch index) by adding the
    # number of batch items in the tensor we are appending to (so an index
    # of [0, 0, 1] for a value that is being appended to a tensor with 0th dim
    # size 3 would become [3, 0, 1].)
    index[0] += base_dim0_value
    max_dim0_value = max(max_dim0_value, index[0])
    new_indices = np.append(new_indices, [index], axis=0)

# Extend the values array to contain all of the appended values. These will
# be in the same order as the indices added above.
new_values = np.concatenate((target.values, to_append.values), axis=0)

# Create a new dense shape by replacing the value for the 0th dimension
# with the new max dim0 value.
new_dense_shape = list(target.dense_shape)
new_dense_shape[0] = max_dim0_value + 1
new_dense_shape = tuple(new_dense_shape)

exit(sparse_tensor.SparseTensorValue(
    indices=new_indices, values=new_values, dense_shape=new_dense_shape))
