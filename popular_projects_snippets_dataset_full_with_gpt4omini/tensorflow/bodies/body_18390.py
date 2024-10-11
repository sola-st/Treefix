# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs()
data_format = pfor_input.get_attr("data_format")
y_backprop = pfor_input.stacked_input(0)
y_backprop, _, _ = _channel_flatten_input(y_backprop, data_format)
x = pfor_input.stacked_input(1)
x, x_reverse_order, x_reverse_shape = _channel_flatten_input(x, data_format)
inputs = [y_backprop, x] + [
    array_ops.reshape(pfor_input.stacked_input(i), [-1])
    for i in range(2, pfor_input.num_inputs)
]
outputs = _create_op(
    pfor_input.op_type,
    inputs, [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
x_backprop = outputs[0]
x_backprop = array_ops.reshape(x_backprop, x_reverse_shape)
x_backprop = array_ops.transpose(x_backprop, x_reverse_order)
n = pfor_input.pfor.loop_len_vector
outputs = [_unflatten_first_dim(x, n) for x in outputs[1:]]
outputs = [x_backprop] + outputs
exit([wrap(output, True) for output in outputs])
