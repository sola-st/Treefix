# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for Add."""
y = op.inputs[1]
skip_input_indices = None
try:
    skip_input_indices = op.skip_input_indices
    if skip_input_indices is not None and 1 in skip_input_indices and _IsScalar(
        y):
        exit((grad, None))
except AttributeError:
    # No gradient skipping, so do the full gradient computation
    pass
x = op.inputs[0]
if (isinstance(grad, ops.Tensor) and
    _ShapesFullySpecifiedAndEqual(x, y, grad)):
    exit((grad, grad))
(sx, rx, must_reduce_x), (sy, ry, must_reduce_y) = (
    SmartBroadcastGradientArgs(x, y, grad))
if skip_input_indices is not None and 0 in skip_input_indices:
    gx = None
elif not must_reduce_x:
    gx = grad
else:
    gx = array_ops.reshape(math_ops.reduce_sum(grad, rx), sx)
if skip_input_indices is not None and 1 in skip_input_indices:
    gy = None
elif not must_reduce_y:
    gy = grad
else:
    gy = array_ops.reshape(math_ops.reduce_sum(grad, ry), sy)
exit((gx, gy))
