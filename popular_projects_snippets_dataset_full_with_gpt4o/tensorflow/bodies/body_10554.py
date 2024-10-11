# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Returns grad * (y*x^(y-1), z*log(x))."""
x = op.inputs[0]
y = op.inputs[1]
skip_input_indices = None
try:
    skip_input_indices = op.skip_input_indices
    # TODO(mrry): If `y` is a constant, we can combine `tf.sub()` and the
    # constant `1` into a single constant op.
    if skip_input_indices is not None and 1 in skip_input_indices and _IsScalar(
        y):
        x = math_ops.conj(x)
        y = math_ops.conj(y)
        exit((grad * y * math_ops.pow(x, y - 1), None))

except AttributeError:
    # No gradient skipping, so do the full gradient computation
    pass

(sx, rx, must_reduce_x), (sy, ry, must_reduce_y) = (
    SmartBroadcastGradientArgs(x, y, grad))
x = math_ops.conj(x)
y = math_ops.conj(y)

if skip_input_indices is None or 0 not in skip_input_indices:
    gx = grad * y * math_ops.pow(x, y - 1)
    if must_reduce_x:
        gx = array_ops.reshape(math_ops.reduce_sum(gx, rx), sx)
else:
    gx = None

if skip_input_indices is None or 1 not in skip_input_indices:
    z = math_ops.conj(op.outputs[0])

    # Avoid false singularity at x = 0
    if x.dtype.is_complex:
        # real(x) < 0 is fine for the complex case
        mask = math_ops.not_equal(x, 0)
    else:
        # There's no sensible real value to return if x < 0, so return 0
        mask = x > 0
    safe_x = array_ops.where(mask, x, array_ops.ones_like(x))
    log_x = array_ops.where(mask, math_ops.log(safe_x), array_ops.zeros_like(x))
    gy = grad * z * log_x
    if must_reduce_y:
        gy = array_ops.reshape(math_ops.reduce_sum(gy, ry), sy)
else:
    gy = None

exit((gx, gy))
