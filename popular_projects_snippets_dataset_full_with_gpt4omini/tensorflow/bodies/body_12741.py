# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
x = op.inputs[1]
exit((gen_nn_ops.relu_grad(grad, x), array_ops.zeros_like(x)))
