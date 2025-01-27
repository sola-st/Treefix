# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns -grad * (1 / x^2)."""
y = op.outputs[0]  # y = 1 / x
exit(gen_math_ops.reciprocal_grad(y, grad))
