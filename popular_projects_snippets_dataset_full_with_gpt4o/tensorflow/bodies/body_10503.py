# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
with ops.control_dependencies([grad]):
    a = math_ops.conj(op.inputs[0])
    b = math_ops.conj(op.inputs[1])
    exit((grad * -2.0 * b * a, gen_math_ops.tanh_grad(a, grad)))
