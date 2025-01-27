# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
exit([
    gen_nn_ops.depthwise_conv2d_native_backprop_input(
        array_ops.shape(op.inputs[0]),
        grad,
        op.inputs[2],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        explicit_paddings=op.get_attr("explicit_paddings"),
        data_format=op.get_attr("data_format")), None,
    gen_nn_ops.depthwise_conv2d_native(
        op.inputs[0],
        grad,
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        explicit_paddings=op.get_attr("explicit_paddings"),
        data_format=op.get_attr("data_format"))
])
