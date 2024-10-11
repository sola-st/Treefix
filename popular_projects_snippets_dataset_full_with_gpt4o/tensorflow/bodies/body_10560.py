# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
c = op.inputs[0]
x = op.inputs[1]
zeros = array_ops.zeros_like(x)
exit((None, array_ops.where(c, grad, zeros), array_ops.where(
    c, zeros, grad)))
