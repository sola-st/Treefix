# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * 1/ (1 + x^2)."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    x = math_ops.conj(x)
    x2 = math_ops.square(x)
    one = constant_op.constant(1, dtype=grad.dtype)
    inv = math_ops.reciprocal(math_ops.add(one, x2))
    exit(grad * inv)
