# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns 'grad' as the real part and set the imaginary part 0."""
zero = constant_op.constant(0, dtype=grad.dtype)
exit(math_ops.complex(grad, zero))
