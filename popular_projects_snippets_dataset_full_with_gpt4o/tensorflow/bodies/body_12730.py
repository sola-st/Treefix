# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
elu_x = op.inputs[1]
exit((gen_nn_ops.elu_grad(grad, elu_x),
        array_ops.where(
            elu_x < 0, grad * op.inputs[0], array_ops.zeros_like(elu_x))))
