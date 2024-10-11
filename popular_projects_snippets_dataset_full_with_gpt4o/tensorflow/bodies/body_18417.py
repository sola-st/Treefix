# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs()
axis = pfor_input.get_attr("axis")
if axis >= 0:
    axis += 1
exit(wrap(
    array_ops.stack([x.t for x in pfor_input.inputs], axis=axis), True))
