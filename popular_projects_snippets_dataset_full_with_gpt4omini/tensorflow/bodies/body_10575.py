# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns 'grad' as the imaginary part and set the real part 0."""
zero = constant_op.constant(0, dtype=grad.dtype)
exit(math_ops.complex(zero, grad))
