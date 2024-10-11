# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
with ops.control_dependencies([grad]):
    a = math_ops.conj(op.inputs[0])
    b = math_ops.conj(op.inputs[1])
    gb = grad * b
    exit((gb - 2.0 * gb * a, gen_math_ops.sigmoid_grad(a, grad)))
