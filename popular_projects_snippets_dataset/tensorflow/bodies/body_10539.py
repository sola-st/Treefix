# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * -1/sqrt(1-x^2)."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    x = math_ops.conj(x)
    x2 = math_ops.square(x)
    one = constant_op.constant(1, dtype=grad.dtype)
    den = math_ops.sqrt(math_ops.subtract(one, x2))
    inv = math_ops.reciprocal(den)
    exit(-grad * inv)
