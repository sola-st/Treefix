# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns backprop gradient for f(a,b) = -0.5 * b * conj(a)^3."""
a = op.inputs[0]  # a = x^{-1/2}
b = op.inputs[1]  # backprop gradient for a
with ops.control_dependencies([grad]):
    ca = math_ops.conj(a)
    cg = math_ops.conj(grad)
    grad_a = -1.5 * cg * b * math_ops.square(ca)
    grad_b = gen_math_ops.rsqrt_grad(ca, grad)
    exit((grad_a, grad_b))
