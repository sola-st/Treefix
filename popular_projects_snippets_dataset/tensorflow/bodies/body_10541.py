# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * x / (x^2 + y^2), grad * -y / (x^2 + y^2)."""
y = op.inputs[0]
x = op.inputs[1]
with ops.control_dependencies([grad]):
    grad_inv = grad / (math_ops.square(x) + math_ops.square(y))
    exit((x * grad_inv, -y * grad_inv))
