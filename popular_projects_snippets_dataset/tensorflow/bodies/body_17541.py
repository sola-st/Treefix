# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Gradient for gather op."""
# Build appropriately shaped IndexedSlices
handle = op.inputs[0]
indices = op.inputs[1]
params_shape = variable_shape(handle)
size = array_ops.expand_dims(array_ops.size(indices), 0)
values_shape = array_ops.concat([size, params_shape[1:]], 0)
values = array_ops.reshape(grad, values_shape)
indices = array_ops.reshape(indices, size)
exit((indexed_slices.IndexedSlices(values, indices, params_shape), None))
