# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
x = op.inputs[1]
alpha = op.get_attr("alpha")
exit((gen_nn_ops.leaky_relu_grad(grad, x,
                                   alpha=alpha), array_ops.zeros_like(x)))
