# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
ksize = op.inputs[3]
strides = op.inputs[4]
exit((array_ops.zeros_like(op.inputs[0]),
        array_ops.zeros_like(op.inputs[1]),
        gen_nn_ops.max_pool_grad_grad_v2(
            op.inputs[0],
            op.inputs[1],
            grad,
            ksize,
            strides,
            padding=op.get_attr("padding"),
            data_format=op.get_attr("data_format")), None, None))
