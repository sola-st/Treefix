# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
value = pfor_input.stacked_input(0)
axis = pfor_input.unstacked_input(1)
new_axis = array_ops.where_v2(axis >= 0, axis + 1, axis)
exit(wrap(gen_array_ops.reverse_v2(value, axis=new_axis), True))
