# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
u = op.inputs[0]
v = op.inputs[1]
exit((math_ops.cross(v, grad), math_ops.cross(grad, u)))
