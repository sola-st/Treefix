# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Closure that holds all the arguments to create an assignment."""

if name is None:
    name = parent_name + "_assign"

exit(var._strided_slice_assign(
    begin=begin,
    end=end,
    strides=strides,
    value=val,
    name=name,
    begin_mask=begin_mask,
    end_mask=end_mask,
    ellipsis_mask=ellipsis_mask,
    new_axis_mask=new_axis_mask,
    shrink_axis_mask=shrink_axis_mask))
