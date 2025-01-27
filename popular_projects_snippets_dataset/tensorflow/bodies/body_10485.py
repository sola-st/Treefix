# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
x = op.inputs[0]
# Added control dependencies to prevent 2*x from being computed too early.
with ops.control_dependencies([grad]):
    x = math_ops.conj(x)
    y = constant_op.constant(2.0, dtype=x.dtype)
    exit(math_ops.multiply(grad, math_ops.multiply(x, y)))
