# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for GatherV2 op."""
# params can be large, so colocate the shape calculation with it.
#
# params can be very large for sparse model, array_ops.shape raises
# exception on the Windows platform when any dimension is larger than
# int32. params_shape is not used in optimizer apply_sparse gradients,
# so it's fine to convert it back to int32 regardless of truncation.
params = op.inputs[0]
with ops.colocate_with(params):
    params_shape = array_ops.shape(params, out_type=ops.dtypes.int64)
    params_shape = math_ops.cast(params_shape, dtypes.int32)

indices = op.inputs[1]
indices_size = array_ops.expand_dims(array_ops.size(indices), 0)
axis = op.inputs[2]
axis_static = tensor_util.constant_value(axis)
batch_dims = int(op.get_attr("batch_dims"))

if batch_dims < 0:
    if indices.shape.ndims is None:
        raise ValueError(
            f"Currently, it is unsupported to take the gradient of tf.gather "
            f"when batch_dims < 0 and the rank of the indices is unknown. Please "
            f"pass a positive batch_dims or use tf.ensure_shape to update the "
            f"shape of indices when calling tf.gather. Got "
            f"batch_dims={batch_dims} and indices={indices}")
    batch_dims += indices.shape.ndims

# For axis 0 gathers, build an appropriately shaped IndexedSlices.
if axis_static == 0:
    if context.executing_eagerly():
        with ops.device(indices_size.device):
            params_tail_shape = array_ops.identity(params_shape)[1:]
    else:
        params_tail_shape = params_shape[1:]
    values_shape = array_ops.concat([indices_size, params_tail_shape], 0)
    values = array_ops.reshape(
        _IndexedSlicesToTensorNoWarning(grad), values_shape)
    indices = array_ops.reshape(indices, indices_size)
    params_grad = indexed_slices_lib.IndexedSlices(values, indices,
                                                   params_shape)
else:
    # Handle axis by transposing the axis dimension to be the first non-batch
    # dimension, compute the gradient and transpose the result back.
    outer_shape = params_shape[:axis]
    inner_shape = params_shape[axis:][1:]
    values_shape = array_ops.concat([outer_shape, [-1], inner_shape], 0)

    values_dims = array_ops.size(values_shape)
    axis_dims = array_ops.size(outer_shape)

    outer_batches_indices = math_ops.range(batch_dims)
    batch_axis_indices = math_ops.range(batch_dims, axis_dims)
    inner_axes_indices = math_ops.range(axis_dims + 1, values_dims)

    values = array_ops.reshape(
        _IndexedSlicesToTensorNoWarning(grad), values_shape)

    # Move values[axis] up to values[batch_dims]
    transpose_dims = array_ops.concat([
        outer_batches_indices, [axis_dims], batch_axis_indices,
        inner_axes_indices
    ], 0)
    values_transpose = array_ops.transpose(values, transpose_dims)
    params_shape_transpose = array_ops.gather(params_shape, transpose_dims)

    params_grad = _BatchGatherGrad(params_shape_transpose, values_transpose,
                                   indices, batch_dims, params_shape[axis])

    # Inverts the above transpose by moving dimension batch_dims back to its
    # original position.
    invert_transpose_dims = array_ops.concat([
        outer_batches_indices, batch_axis_indices + 1, [batch_dims],
        inner_axes_indices
    ], 0)
    params_grad = array_ops.transpose(params_grad, invert_transpose_dims)

exit([params_grad, None, None])
