# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clip_ops.py
"""Returns grad of clip_by_value."""
x = op.inputs[0]
y = op.inputs[1]
z = op.inputs[2]
gdtype = grad.dtype
sx = array_ops.shape(x)
sy = array_ops.shape(y)
sz = array_ops.shape(z)
gradshape = array_ops.shape(grad)
zeros = array_ops.zeros(gradshape, gdtype)
xymask = math_ops.less(x, y)
xzmask = math_ops.greater(x, z)
rx, ry = gen_array_ops.broadcast_gradient_args(sx, sy)
rx, rz = gen_array_ops.broadcast_gradient_args(sx, sz)
xgrad = array_ops.where(math_ops.logical_or(xymask, xzmask), zeros, grad)
ygrad = array_ops.where(xymask, grad, zeros)
zgrad = array_ops.where(xzmask, grad, zeros)
gx = array_ops.reshape(math_ops.reduce_sum(xgrad, rx), sx)
gy = array_ops.reshape(math_ops.reduce_sum(ygrad, ry), sy)
gz = array_ops.reshape(math_ops.reduce_sum(zgrad, rz), sz)
exit((gx, gy, gz))
