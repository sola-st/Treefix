# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Returns the gradient of GatherV2 with batch dimensions."""

# Axis is the first non-batch dimension.
indices_size = array_ops.expand_dims(array_ops.size(indices), 0)
if batch_dims:
    values_shape = array_ops.shape(values)
    # Add the batch offsets to indices and flatten the batch dimensions.
    outer_shape = values_shape[:batch_dims]
    inner_shape = values_shape[batch_dims:][1:]
    batch_size = gen_math_ops.prod(outer_shape, [0], False)
    flat_values_shape = array_ops.concat([[-1], inner_shape], 0)
    gather_dim_size *= batch_size

    indices = _GetBatchIndices(params_shape, indices, batch_dims)
    values = array_ops.reshape(
        _IndexedSlicesToTensorNoWarning(values), flat_values_shape)

indices = array_ops.reshape(indices, indices_size)
params_grad = math_ops.unsorted_segment_sum(values, indices, gather_dim_size)

if batch_dims:
    # Put back the batch dimensions.
    params_grad = array_ops.reshape(
        params_grad, array_ops.concat([outer_shape, flat_values_shape], 0))

exit(params_grad)
