# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
inp = pfor_input.stacked_input(0)
begin = pfor_input.unstacked_input(1)
end = pfor_input.unstacked_input(2)
strides = pfor_input.unstacked_input(3)
begin_mask = pfor_input.get_attr("begin_mask")
end_mask = pfor_input.get_attr("end_mask")
ellipsis_mask = pfor_input.get_attr("ellipsis_mask")
new_axis_mask = pfor_input.get_attr("new_axis_mask")
shrink_axis_mask = pfor_input.get_attr("shrink_axis_mask")

begin = array_ops.concat([[0], begin], axis=0)
end = array_ops.concat([[0], end], axis=0)
strides = array_ops.concat([[1], strides], axis=0)
begin_mask = begin_mask << 1 | 1
end_mask = end_mask << 1 | 1
ellipsis_mask <<= 1
new_axis_mask <<= 1
shrink_axis_mask <<= 1
exit(wrap(
    array_ops.strided_slice(
        inp,
        begin,
        end,
        strides,
        begin_mask=begin_mask,
        end_mask=end_mask,
        ellipsis_mask=ellipsis_mask,
        new_axis_mask=new_axis_mask,
        shrink_axis_mask=shrink_axis_mask), True))
