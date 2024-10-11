# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
b = op.inputs[1]
# op.output[0]: y = -b * conj(a)^2
with ops.control_dependencies([grad]):
    ca = math_ops.conj(op.inputs[0])
    cg = math_ops.conj(grad)
    exit((cg * -2.0 * b * ca, gen_math_ops.reciprocal_grad(ca, grad)))
