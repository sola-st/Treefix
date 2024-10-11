# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
axis = op.inputs[1]
exclusive = op.get_attr("exclusive")
reverse = op.get_attr("reverse")
exit([
    math_ops.cumsum(grad, axis, exclusive=exclusive, reverse=not reverse),
    None
])
