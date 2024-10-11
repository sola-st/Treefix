# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns -grad / (Im(x) + iRe(x))"""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    re = math_ops.real(x)
    im = math_ops.imag(x)
    z = math_ops.reciprocal(math_ops.complex(im, re))
    zero = constant_op.constant(0, dtype=grad.dtype)
    complex_grad = math_ops.complex(grad, zero)
    exit(-complex_grad * z)
