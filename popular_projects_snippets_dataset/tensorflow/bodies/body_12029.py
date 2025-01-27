# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for StridedSliceGrad op."""
begin = op.inputs[1]
end = op.inputs[2]
strides = op.inputs[3]

exit((None, None, None, None, array_ops.strided_slice(
    grad,
    begin,
    end,
    strides,
    begin_mask=op.get_attr("begin_mask"),
    end_mask=op.get_attr("end_mask"),
    ellipsis_mask=op.get_attr("ellipsis_mask"),
    new_axis_mask=op.get_attr("new_axis_mask"),
    shrink_axis_mask=op.get_attr("shrink_axis_mask"))))
