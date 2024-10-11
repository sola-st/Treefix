# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""Gradient function for Conv2D."""
dilations = op.get_attr("dilations")
strides = op.get_attr("strides")
padding = op.get_attr("padding")
explicit_paddings = op.get_attr("explicit_paddings")
use_cudnn_on_gpu = op.get_attr("use_cudnn_on_gpu")
data_format = op.get_attr("data_format")
shape_0, shape_1 = array_ops.shape_n([op.inputs[0], op.inputs[1]])

# We call the gen_nn_ops backprop functions instead of nn_ops backprop
# functions for performance reasons in Eager mode. gen_nn_ops functions take a
# `explicit_paddings` parameter, but nn_ops functions do not. So if we were
# to use the nn_ops functions, we would have to convert `padding` and
# `explicit_paddings` into a single `padding` parameter, increasing overhead
# in Eager mode.
exit([
    gen_nn_ops.conv2d_backprop_input(
        shape_0,
        op.inputs[1],
        grad,
        dilations=dilations,
        strides=strides,
        padding=padding,
        explicit_paddings=explicit_paddings,
        use_cudnn_on_gpu=use_cudnn_on_gpu,
        data_format=data_format),
    gen_nn_ops.conv2d_backprop_filter(
        op.inputs[0],
        shape_1,
        grad,
        dilations=dilations,
        strides=strides,
        padding=padding,
        explicit_paddings=explicit_paddings,
        use_cudnn_on_gpu=use_cudnn_on_gpu,
        data_format=data_format)
])
