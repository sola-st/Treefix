# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
shape = pfor_input.unstacked_input(0)
begin = pfor_input.unstacked_input(1)
end = pfor_input.unstacked_input(2)
strides = pfor_input.unstacked_input(3)
dy = pfor_input.stacked_input(4)
begin_mask = pfor_input.get_attr("begin_mask")
end_mask = pfor_input.get_attr("end_mask")
ellipsis_mask = pfor_input.get_attr("ellipsis_mask")
new_axis_mask = pfor_input.get_attr("new_axis_mask")
shrink_axis_mask = pfor_input.get_attr("shrink_axis_mask")

shape = array_ops.concat(
    [math_ops.cast(pfor_input.pfor.loop_len_vector, shape.dtype), shape],
    axis=0)
begin = array_ops.concat([[0], begin], axis=0)
end = array_ops.concat([[0], end], axis=0)
strides = array_ops.concat([[1], strides], axis=0)
begin_mask = begin_mask << 1 | 1
end_mask = end_mask << 1 | 1
ellipsis_mask <<= 1
new_axis_mask <<= 1
shrink_axis_mask <<= 1
exit(wrap(
    array_ops.strided_slice_grad(
        shape,
        begin,
        end,
        strides,
        dy,
        begin_mask=begin_mask,
        end_mask=end_mask,
        ellipsis_mask=ellipsis_mask,
        new_axis_mask=new_axis_mask,
        shrink_axis_mask=shrink_axis_mask), True))
