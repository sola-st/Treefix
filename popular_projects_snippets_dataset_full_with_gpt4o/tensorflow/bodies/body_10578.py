# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns the gradient of ComplexAbs."""
exit(math_ops.div_no_nan(
    math_ops.complex(
        grad, array_ops.zeros_like(grad)) * op.inputs[0],
    math_ops.complex(
        op.outputs[0], array_ops.zeros_like(op.outputs[0]))))
