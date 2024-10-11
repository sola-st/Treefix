# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
is_training = pfor_input.get_attr("is_training")
# When BatchNorm is used with training=False, mean and variance are provided
# externally and used as is by the op. Thus, we can merge the S and N
# dimensions as we do for regular operations.
# When BatchNorm is used with training=True, mean and variance are computed
# for each channel across the batch dimension (first one). If we merge S and N
# dimensions, mean and variances will be computed over a larger set. So, we
# merge the S and C dimensions instead.
if not is_training:
    # We return zeros for batch_mean and batch_variance output. Note that CPU
    # and GPU seem to have different behavior for those two outputs. CPU outputs
    # zero because these values are not used during inference. GPU outputs
    # something, probably real means and variances.
    inputs = _inputs_with_flattening(pfor_input, [0])
    outputs = _create_op(
        pfor_input.op_type,
        inputs, [x.dtype for x in pfor_input.outputs],
        attrs=pfor_input.op.node_def.attr).outputs
    y = outputs[0]
    n = pfor_input.pfor.loop_len_vector
    y = _unflatten_first_dim(y, n)
    mean = pfor_input.unstacked_input(3)
    zeros = array_ops.zeros_like(mean)
    exit([wrap(y, True)] + [wrap(zeros, False)] * 5)

pfor_input.stack_inputs()
data_format = pfor_input.get_attr("data_format")
# We merge the first dimension with the "C" dimension, run FusedBatchNormV3,
# and then transpose back.
x = pfor_input.stacked_input(0)
x, reverse_order, reverse_shape = _channel_flatten_input(x, data_format)
# Note that we stack all the other inputs as well so that they are the same
# size as the new size of the channel dimension.
inputs = [x] + [
    array_ops.reshape(pfor_input.stacked_input(i), [-1])
    for i in range(1, pfor_input.num_inputs)
]
outputs = _create_op(
    pfor_input.op_type,
    inputs, [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
y = outputs[0]
y = array_ops.reshape(y, reverse_shape)
y = array_ops.transpose(y, reverse_order)
n = pfor_input.pfor.loop_len_vector
outputs = [_unflatten_first_dim(x, n) for x in outputs[1:]]
outputs = [y] + outputs
exit([wrap(x, True) for x in outputs])
