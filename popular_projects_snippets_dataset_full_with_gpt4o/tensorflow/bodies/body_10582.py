# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
x = op.inputs[0]
axis = op.inputs[1]
exclusive = op.get_attr("exclusive")
reverse = op.get_attr("reverse")

prod = math_ops.cumprod(x, axis, exclusive=exclusive, reverse=reverse)
out = math_ops.cumsum(
    prod * grad, axis, exclusive=exclusive, reverse=not reverse)
exit([math_ops.div_no_nan(out, x), None])
