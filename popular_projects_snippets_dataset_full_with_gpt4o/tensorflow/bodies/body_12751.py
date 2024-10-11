# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
exit(gen_nn_ops.max_pool_grad(
    op.inputs[0],
    op.outputs[0],
    grad,
    op.get_attr("ksize"),
    op.get_attr("strides"),
    padding=op.get_attr("padding"),
    explicit_paddings=op.get_attr("explicit_paddings"),
    data_format=op.get_attr("data_format")))
