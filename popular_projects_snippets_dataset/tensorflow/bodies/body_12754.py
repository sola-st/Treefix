# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
exit((array_ops.zeros_like(op.inputs[0]),
        array_ops.zeros_like(op.inputs[1]),
        gen_nn_ops.max_pool_grad_grad(
            op.inputs[0],
            op.inputs[1],
            grad,
            op.get_attr("ksize"),
            op.get_attr("strides"),
            padding=op.get_attr("padding"),
            data_format=op.get_attr("data_format"))))
