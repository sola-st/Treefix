# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
c = op.inputs[0]
x = op.inputs[1]
y = op.inputs[2]
zeros = array_ops.zeros([], dtype=grad.dtype.base_dtype)
gx = array_ops.where_v2(c, grad, zeros)
x_shape = array_ops.shape(x)
output_shape = array_ops.shape(op.outputs[0])
# Reduce away broadcasted leading dims.
reduce_x, _ = gen_array_ops.broadcast_gradient_args(x_shape, output_shape)
gx = math_ops.reduce_sum(gx, keepdims=True, axis=reduce_x)
gx = array_ops.reshape(gx, x_shape)

gy = array_ops.where_v2(c, zeros, grad)
y_shape = array_ops.shape(y)
# Reduce away broadcasted leading dims.
reduce_y, _ = gen_array_ops.broadcast_gradient_args(y_shape, output_shape)
gy = math_ops.reduce_sum(gy, keepdims=True, axis=reduce_y)
gy = array_ops.reshape(gy, y_shape)

exit((None, gx, gy))
