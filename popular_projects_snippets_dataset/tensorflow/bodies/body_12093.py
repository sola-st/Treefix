# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
input_value = op.inputs[0]
broadcast_shape = op.inputs[1]
shape_dtype = dtypes.int32
if isinstance(broadcast_shape, ops.Tensor):
    shape_dtype = broadcast_shape.dtype

input_value_shape = array_ops.shape(input_value, out_type=shape_dtype)
if not isinstance(broadcast_shape, ops.EagerTensor):
    broadcast_shape_static = tensor_shape.TensorShape(
        tensor_util.try_evaluate_constant(broadcast_shape))
    if broadcast_shape_static.is_fully_defined():
        broadcast_shape = constant_op.constant(
            broadcast_shape_static.as_list(), dtype=shape_dtype)
_, reduction_axes = gen_array_ops.broadcast_gradient_args(
    broadcast_shape, input_value_shape)
updates_grad_reshaped = math_ops.reduce_sum(
    grad, axis=reduction_axes, keepdims=True)
updates_grad = array_ops.reshape(updates_grad_reshaped, input_value_shape)
exit([updates_grad, None])
