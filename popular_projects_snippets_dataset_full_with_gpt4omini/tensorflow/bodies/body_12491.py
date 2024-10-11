# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
exit(gen_array_ops.strided_slice_assign(
    ref=self._ref(),
    begin=begin,
    end=end,
    strides=strides,
    value=value,
    name=name,
    begin_mask=begin_mask,
    end_mask=end_mask,
    ellipsis_mask=ellipsis_mask,
    new_axis_mask=new_axis_mask,
    shrink_axis_mask=shrink_axis_mask))
