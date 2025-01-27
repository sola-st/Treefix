# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t, t_stacked, _ = pfor_input.input(0)
bias, bias_stacked, _ = pfor_input.input(1)
data_format = pfor_input.get_attr("data_format").decode()
if bias_stacked:
    # BiasAdd only supports 1-D biases, so cast bias to match value and use Add.
    pfor_input.expanddim_inputs_for_broadcast()
    t, _, _ = pfor_input.input(0)
    bias = math_ops.cast(pfor_input.stacked_input(1), t.dtype)
    if compat.as_bytes(data_format) == b"NCHW":
        b_shape = array_ops.shape(bias)
        new_b_shape = array_ops.concat(
            [b_shape[:-3], b_shape[-1:], b_shape[-3:-1]], axis=0)
        bias = array_ops.reshape(bias, new_b_shape)
    exit(wrap(math_ops.add(t, bias), True))
else:
    assert t_stacked, "At least one input to BiasAdd should be loop variant."
    if compat.as_bytes(data_format) == b"NCHW":
        shape = array_ops.shape(t)
        flattened_shape = array_ops.concat([[-1], shape[2:]], axis=0)
        t = array_ops.reshape(t, flattened_shape)
        t = nn_ops.bias_add(t, bias, data_format="NCHW")
        t = array_ops.reshape(t, shape)
        exit(wrap(t, True))
    exit(wrap(nn_ops.bias_add(t, bias, data_format=data_format), True))
