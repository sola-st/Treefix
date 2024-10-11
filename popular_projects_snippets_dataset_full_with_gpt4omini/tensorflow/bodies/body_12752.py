# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
ksize = op.inputs[1]
strides = op.inputs[2]
exit((gen_nn_ops.max_pool_grad_v2(
    op.inputs[0],
    op.outputs[0],
    grad,
    ksize,
    strides,
    padding=op.get_attr("padding"),
    data_format=op.get_attr("data_format")), None, None))
