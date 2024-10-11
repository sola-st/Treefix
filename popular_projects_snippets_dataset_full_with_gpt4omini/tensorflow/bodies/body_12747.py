# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
exit([
    nn_ops.dilation2d_backprop_input(op.inputs[0], op.inputs[1], grad,
                                     op.get_attr("strides"),
                                     op.get_attr("rates"),
                                     op.get_attr("padding")),
    nn_ops.dilation2d_backprop_filter(op.inputs[0], op.inputs[1], grad,
                                      op.get_attr("strides"),
                                      op.get_attr("rates"),
                                      op.get_attr("padding"))
])
