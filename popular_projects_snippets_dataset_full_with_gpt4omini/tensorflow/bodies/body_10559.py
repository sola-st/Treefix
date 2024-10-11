# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns the gradient for (x-y)^2."""
x = op.inputs[0]
y = op.inputs[1]
skip_input_indices = None
try:
    skip_input_indices = op.skip_input_indices
except AttributeError:
    # No gradient skipping, so do the full gradient computation
    pass

with ops.control_dependencies([grad]):
    # The parens ensure that if grad is IndexedSlices, it'll get multiplied by
    # Tensor (not a number like 2.0) which causes it to convert to Tensor.
    x_grad = math_ops.scalar_mul(2.0, grad) * (x - y)

if (isinstance(grad, ops.Tensor) and
    _ShapesFullySpecifiedAndEqual(x, y, grad)):
    exit((x_grad, -x_grad))

(sx, rx, must_reduce_x), (sy, ry, must_reduce_y) = (
    SmartBroadcastGradientArgs(x, y, grad))

if skip_input_indices is not None and 0 in skip_input_indices:
    gx = None
elif must_reduce_x:
    gx = array_ops.reshape(math_ops.reduce_sum(x_grad, rx), sx)
else:
    gx = x_grad

if skip_input_indices is not None and 1 in skip_input_indices:
    gy = None
elif must_reduce_y:
    gy = -array_ops.reshape(math_ops.reduce_sum(x_grad, ry), sy)
else:
    gy = -x_grad
exit((gx, gy))
