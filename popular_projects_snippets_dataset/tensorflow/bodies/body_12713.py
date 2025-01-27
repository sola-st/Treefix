# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
# We call the gen_nn_ops backprop functions instead of nn_ops backprop
# functions for performance reasons in Eager mode. See _Conv2DGrad.
exit([
    gen_nn_ops.conv2d_backprop_input(
        array_ops.shape(op.inputs[0]),
        grad,
        op.inputs[2],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        explicit_paddings=op.get_attr("explicit_paddings"),
        use_cudnn_on_gpu=op.get_attr("use_cudnn_on_gpu"),
        data_format=op.get_attr("data_format").decode()), None,
    gen_nn_ops.conv2d(
        op.inputs[0],
        grad,
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        explicit_paddings=op.get_attr("explicit_paddings"),
        use_cudnn_on_gpu=op.get_attr("use_cudnn_on_gpu"),
        data_format=op.get_attr("data_format").decode())
])
