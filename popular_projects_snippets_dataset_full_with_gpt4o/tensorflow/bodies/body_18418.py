# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
value = pfor_input.stacked_input(0)
axis = pfor_input.get_attr("axis")
if axis >= 0:
    axis += 1
num = pfor_input.get_attr("num")
exit([wrap(x, True) for x in array_ops.unstack(value, axis=axis, num=num)])
