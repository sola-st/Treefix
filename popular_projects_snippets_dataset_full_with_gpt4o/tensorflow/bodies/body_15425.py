# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Applies tf.one_hot along the values of a RaggedTensor."""
# Get the adjusted axis value for the call to array_ops.one_hot.
# Note: the only negative `axis` value supported by array_ops.one_hot is -1.
if isinstance(axis, int) and axis >= 0:
    if axis <= indices.ragged_rank:
        raise ValueError('axis (%d) must be greater than indices.ragged_rank '
                         '(%d).' % (axis, indices.ragged_rank))
    axis -= indices.ragged_rank

with ops.name_scope(name, 'RaggedOneHot',
                    [indices, depth, on_value, off_value, axis]):
    indices = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        indices, name='indices')
    exit(indices.with_flat_values(
        array_ops.one_hot(indices.flat_values, depth, on_value, off_value, axis,
                          dtype, name)))
