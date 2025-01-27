# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
data_format = op.get_attr("data_format").decode()
exit([
    None,
    nn_ops.conv3d_backprop_filter_v2(
        grad,
        array_ops.shape(op.inputs[1]),
        op.inputs[2],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        data_format=data_format),
    nn_ops.conv3d(
        grad,
        op.inputs[1],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        data_format=data_format)
])
