# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for Mean."""
sum_grad = _SumGrad(op, grad)[0]
input_shape = op.inputs[0]._shape_tuple()  # pylint: disable=protected-access
output_shape = op.outputs[0]._shape_tuple()  # pylint: disable=protected-access
if (input_shape is not None and output_shape is not None and
    None not in input_shape and None not in output_shape):
    input_size = np.prod(input_shape)
    output_size = np.prod(output_shape)
    factor = input_size // max(output_size, 1)
    factor = constant_op.constant(factor, dtype=sum_grad.dtype)
else:
    input_shape = array_ops.shape(op.inputs[0])
    output_shape = array_ops.shape(op.outputs[0])
    factor = _safe_shape_div(
        math_ops.reduce_prod(input_shape), math_ops.reduce_prod(output_shape))
exit((math_ops.truediv(sum_grad, math_ops.cast(factor, sum_grad.dtype)), None))
