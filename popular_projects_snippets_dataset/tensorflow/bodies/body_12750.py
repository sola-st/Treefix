# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
exit((array_ops.stop_gradient(op.inputs[0]),
        gen_nn_ops.avg_pool(
            grad,
            op.get_attr("ksize"),
            op.get_attr("strides"),
            op.get_attr("padding"),
            data_format=op.get_attr("data_format"))))
