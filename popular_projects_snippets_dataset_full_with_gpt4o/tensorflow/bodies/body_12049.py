# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for Gather op."""
# params can be large, so colocate the shape calculation with it.
params = op.inputs[0]
with ops.colocate_with(params):
    params_shape = array_ops.shape(params)

# Build appropriately shaped IndexedSlices
indices = op.inputs[1]
size = array_ops.expand_dims(array_ops.size(indices), 0)
values_shape = array_ops.concat([size, params_shape[1:]], 0)
values = array_ops.reshape(
    _IndexedSlicesToTensorNoWarning(grad), values_shape)
indices = array_ops.reshape(indices, size)
exit([indexed_slices_lib.IndexedSlices(values, indices, params_shape), None])
