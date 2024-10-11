# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of spence(x) with respect to its argument."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    partial_x = math_ops.log(x) / (1 - x)
    partial_x = array_ops.where(
        math_ops.equal(x, 1.), -array_ops.ones_like(x), partial_x)  # pylint: disable=invalid-unary-operand-type
    exit(grad * partial_x)
