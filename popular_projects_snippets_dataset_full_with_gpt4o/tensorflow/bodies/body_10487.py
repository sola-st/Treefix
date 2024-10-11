# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
a = op.inputs[0]
y = op.outputs[0]  # y = 0.5 * b / conj(a)
with ops.control_dependencies([grad]):
    ga = grad / a
    exit((-math_ops.conj(ga) * y, 0.5 * ga))  # pylint: disable=invalid-unary-operand-type
