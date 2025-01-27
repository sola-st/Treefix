# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
x = op.inputs[0]
exit(grad * math_ops.sign(x))
