# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Factor out the code for the gradient of Maximum or Minimum."""
y = op.inputs[1]
skip_input_indices = None
try:
    skip_input_indices = op.skip_input_indices
    if skip_input_indices is not None and 1 in skip_input_indices and _IsScalar(
        y):
        # When we want to get gradients for the first input only, and the second
        # input tensor is a scalar, we can do a much simpler calculation
        exit(_MaximumMinimumGradInputOnly(op, grad, selector_op))
except AttributeError:
    # No gradient skipping, so do the full gradient computation
    pass
x = op.inputs[0]
sx = array_ops.shape(x)
sy = array_ops.shape(y)
zeros = array_ops.zeros_like(grad)
xmask = selector_op(x, y)
rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
if skip_input_indices is not None and 0 in skip_input_indices:
    gx = None
else:
    xgrad = array_ops.where_v2(xmask, grad, zeros)
    gx = array_ops.reshape(math_ops.reduce_sum(xgrad, rx), sx)

if skip_input_indices is not None and 1 in skip_input_indices:
    gy = None
else:
    ygrad = array_ops.where_v2(xmask, zeros, grad)
    gy = array_ops.reshape(math_ops.reduce_sum(ygrad, ry), sy)

exit((gx, gy))
