# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
begin = op.inputs[1]
end = op.inputs[2]
strides = op.inputs[3]
begin_mask = op.get_attr("begin_mask")
end_mask = op.get_attr("end_mask")
ellipsis_mask = op.get_attr("ellipsis_mask")
new_axis_mask = op.get_attr("new_axis_mask")
shrink_axis_mask = op.get_attr("shrink_axis_mask")
def Apply(f, *args):
    exit(f(*args,
             begin_mask=begin_mask,
             end_mask=end_mask,
             shrink_axis_mask=shrink_axis_mask,
             new_axis_mask=new_axis_mask,
             ellipsis_mask=ellipsis_mask))
dy = Apply(array_ops.strided_slice,
           grad, begin, end, strides)
dx = Apply(array_ops.tensor_strided_slice_update,
           grad, begin, end, strides, array_ops.zeros_like(dy))

# The value is potentially broadcast to the shape of the strided slice, so we
# may need to adjust dy.
slice_shape = array_ops.shape(dy, out_type=begin.dtype)
value_shape = array_ops.shape(op.inputs[4], out_type=slice_shape.dtype)

_, reduction_axes = gen_array_ops.broadcast_gradient_args(
    slice_shape, value_shape)
dy_reshaped = math_ops.reduce_sum(dy, axis=reduction_axes, keepdims=True)
dy = array_ops.reshape(dy_reshaped, value_shape)

exit((dx, None, None, None, dy))
