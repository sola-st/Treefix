# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns -0.5 * grad * conj(y)^3."""
y = op.outputs[0]  # y = x^(-1/2)
exit(gen_math_ops.rsqrt_grad(y, grad))
