# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
axis = pfor_input.unstacked_input(1)
# Shift positive indices by one to account for the extra dimension.
axis += math_ops.cast(axis >= 0, axis.dtype)
exclusive = pfor_input.get_attr("exclusive")
reverse = pfor_input.get_attr("reverse")
exit(wrap(op_func(t, axis, exclusive=exclusive, reverse=reverse), True))
