# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
data_format = op.get_attr("data_format").decode()
exit([
    nn_ops.conv3d_backprop_input_v2(
        array_ops.shape(op.inputs[0]),
        grad,
        op.inputs[2],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        data_format=data_format), None,
    nn_ops.conv3d(
        op.inputs[0],
        grad,
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        data_format=data_format)
])
