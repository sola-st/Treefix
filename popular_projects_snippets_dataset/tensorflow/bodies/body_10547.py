# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""The gradient of scalar multiplication with NaN-suppression."""
x = op.inputs[0]
y = op.inputs[1]
if (isinstance(grad, ops.Tensor) and
    _ShapesFullySpecifiedAndEqual(x, y, grad)):
    exit((gen_math_ops.mul_no_nan(grad, y), gen_math_ops.mul_no_nan(x, grad)))
assert x.dtype.base_dtype == y.dtype.base_dtype, (x.dtype, " vs. ", y.dtype)
sx = array_ops.shape(x)
sy = array_ops.shape(y)
rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
exit((array_ops.reshape(
    math_ops.reduce_sum(gen_math_ops.mul_no_nan(grad, y), rx), sx),
        array_ops.reshape(
            math_ops.reduce_sum(gen_math_ops.mul_no_nan(x, grad), ry), sy)))
