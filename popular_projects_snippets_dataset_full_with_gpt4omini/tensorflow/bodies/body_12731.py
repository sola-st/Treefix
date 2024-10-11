# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
selu_x = op.inputs[1]
exit((gen_nn_ops.selu_grad(grad, selu_x),
        array_ops.where(
            selu_x < 0., grad * op.inputs[0], array_ops.zeros_like(selu_x))))
