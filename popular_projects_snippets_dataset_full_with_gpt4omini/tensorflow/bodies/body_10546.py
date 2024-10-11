# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""The gradient of scalar multiplication."""
y = op.inputs[1]
skip_input_indices = None
try:
    skip_input_indices = op.skip_input_indices
    if skip_input_indices is not None and 1 in skip_input_indices and _IsScalar(
        y):
        exit((gen_math_ops.mul(grad, math_ops.conj(y)), None))
except AttributeError:
    # No gradient skipping, so do the full gradient computation
    pass
x = op.inputs[0]
if (isinstance(grad, ops.Tensor) and
    _ShapesFullySpecifiedAndEqual(x, y, grad) and
    grad.dtype in (dtypes.int32, dtypes.float32)):
    exit((gen_math_ops.mul(grad, y), gen_math_ops.mul(grad, x)))
assert x.dtype.base_dtype == y.dtype.base_dtype, (x.dtype, " vs. ", y.dtype)

(sx, rx, must_reduce_x), (sy, ry, must_reduce_y) = (
    SmartBroadcastGradientArgs(x, y, grad))
x = math_ops.conj(x)
y = math_ops.conj(y)
if skip_input_indices is not None and 0 in skip_input_indices:
    gx = None
elif not must_reduce_x:
    gx = gen_math_ops.mul(grad, y)
else:
    gx = array_ops.reshape(
        math_ops.reduce_sum(gen_math_ops.mul(grad, y), rx), sx)
if skip_input_indices is not None and 1 in skip_input_indices:
    gy = None
elif not must_reduce_y:
    gy = gen_math_ops.mul(x, grad)
else:
    gy = array_ops.reshape(
        math_ops.reduce_sum(gen_math_ops.mul(x, grad), ry), sy)
exit((gx, gy))
