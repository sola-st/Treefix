# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
exit(gen_nn_ops.avg_pool3d_grad(
    array_ops.shape(op.inputs[0]),
    grad,
    ksize=op.get_attr("ksize"),
    strides=op.get_attr("strides"),
    padding=op.get_attr("padding"),
    data_format=op.get_attr("data_format").decode()))
