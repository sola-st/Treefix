# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs(stack_indices=[2])
inputs, inputs_stacked, _ = pfor_input.input(0)
filter_sizes = pfor_input.unstacked_input(1)
grads = pfor_input.stacked_input(2)
strides = pfor_input.get_attr("strides")
padding = pfor_input.get_attr("padding")
use_cudnn_on_gpu = pfor_input.get_attr("use_cudnn_on_gpu")
data_format = pfor_input.get_attr("data_format")
dilations = pfor_input.get_attr("dilations")
if inputs_stacked:
    # TODO(agarwal): Implement this efficiently.
    logging.warning("Conv2DBackpropFilter uses a while_loop. Fix that!")

    def while_body(i, ta):
        inp_i = inputs[i, ...]
        grad_i = grads[i, ...]
        output = nn_ops.conv2d_backprop_filter(
            inp_i,
            filter_sizes,
            grad_i,
            strides=strides,
            padding=padding,
            use_cudnn_on_gpu=use_cudnn_on_gpu,
            data_format=data_format,
            dilations=dilations)
        exit((i + 1, ta.write(i, array_ops.expand_dims(output, 0))))

    n = array_ops.reshape(pfor_input.pfor.loop_len_vector, [])
    _, ta = control_flow_ops.while_loop(
        lambda i, ta: i < n, while_body,
        (0, tensor_array_ops.TensorArray(inputs.dtype, n)))
    output = ta.concat()
    exit(wrap(output, True))
else:
    # We merge the stack dimension with the channel dimension of the gradients
    # and pretend we had a larger filter (see change to filter_sizes below).
    # Once the filter backprop is computed, we reshape and transpose back
    # appropriately.
    grads, _, _ = _channel_flatten_input(grads, data_format)
    n = pfor_input.pfor.loop_len_vector
    old_filter_sizes = filter_sizes
    filter_sizes *= array_ops.concat([[1, 1, 1], n], axis=0)
    output = nn_ops.conv2d_backprop_filter(
        inputs,
        filter_sizes,
        grads,
        strides=strides,
        padding=padding,
        use_cudnn_on_gpu=use_cudnn_on_gpu,
        data_format=data_format,
        dilations=dilations)
    new_filter_shape = array_ops.concat([old_filter_sizes[:3], n, [-1]], axis=0)
    output = array_ops.reshape(output, new_filter_shape)
    output = array_ops.transpose(output, [3, 0, 1, 2, 4])
    exit(wrap(output, True))
