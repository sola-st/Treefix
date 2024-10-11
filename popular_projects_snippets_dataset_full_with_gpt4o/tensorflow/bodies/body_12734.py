# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
x = op.inputs[0]
alpha = op.get_attr("alpha")
exit(gen_nn_ops.leaky_relu_grad(grad, x, alpha=alpha))
