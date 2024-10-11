# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for StridedSlice op."""
begin = op.inputs[1]
end = op.inputs[2]
strides = op.inputs[3]
# StridedSliceGrad requires `x`, `begin`, `end` and `strides` to be of the
# same dtype so we build a shape of the same type as other args.
# Note that the choice of `begin` for specifying `out_type` is arbitrary.
# We could choose any of {begin|end|strides}.dtype since they are required to
# be the same.
x = array_ops.shape(op.inputs[0], out_type=begin.dtype)

x_static = tensor_util.constant_value(x)
x = x_static if x_static is not None else x
begin_static = tensor_util.constant_value(begin)
begin = begin_static if begin_static is not None else begin
end_static = tensor_util.constant_value(end)
end = end_static if end_static is not None else end
strides_static = tensor_util.constant_value(strides)
strides = strides_static if strides_static is not None else strides

exit((array_ops.strided_slice_grad(
    x,
    begin,
    end,
    strides,
    grad,
    begin_mask=op.get_attr("begin_mask"),
    end_mask=op.get_attr("end_mask"),
    ellipsis_mask=op.get_attr("ellipsis_mask"),
    new_axis_mask=op.get_attr("new_axis_mask"),
    shrink_axis_mask=op.get_attr("shrink_axis_mask")), None, None, None))
