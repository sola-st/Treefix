# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
del unused_argmax_grad
exit(gen_nn_ops.max_pool_grad_with_argmax(
    op.inputs[0],
    grad,
    op.outputs[1],
    op.get_attr("ksize"),
    op.get_attr("strides"),
    padding=op.get_attr("padding"),
    include_batch_in_index=op.get_attr("include_batch_in_index")))
