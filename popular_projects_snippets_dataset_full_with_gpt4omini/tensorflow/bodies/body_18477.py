# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
cond, cond_stacked, _ = pfor_input.input(0)
if cond_stacked:
    cond = math_ops.reduce_all(cond)

data_list = [x.t for x in pfor_input.inputs][1:]
exit(_create_op(
    "Assert", [cond] + data_list, [], attrs=pfor_input.op.node_def.attr))
