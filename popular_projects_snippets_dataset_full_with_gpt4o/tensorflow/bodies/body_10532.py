# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * sigmoid(x) * (1 - sigmoid(x))."""
y = op.outputs[0]  # y = sigmoid(x)
with ops.control_dependencies([grad]):
    y = math_ops.conj(y)
    exit(gen_math_ops.sigmoid_grad(y, grad))
