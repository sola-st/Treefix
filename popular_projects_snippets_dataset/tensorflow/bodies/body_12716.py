# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
data_format = op.get_attr("data_format").decode()
shape_0, shape_1 = array_ops.shape_n([op.inputs[0], op.inputs[1]])
exit([
    nn_ops.conv3d_backprop_input_v2(
        shape_0,
        op.inputs[1],
        grad,
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        data_format=data_format),
    nn_ops.conv3d_backprop_filter_v2(
        op.inputs[0],
        shape_1,
        grad,
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        data_format=data_format)
])
