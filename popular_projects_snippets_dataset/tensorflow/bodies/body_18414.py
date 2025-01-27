# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
indices = pfor_input.stacked_input(0)
depth = pfor_input.unstacked_input(1)
on_value = pfor_input.unstacked_input(2)
off_value = pfor_input.unstacked_input(3)
axis = pfor_input.get_attr("axis")
if axis >= 0:
    axis += 1
exit(wrap(
    array_ops.one_hot(indices, depth, on_value, off_value, axis), True))
