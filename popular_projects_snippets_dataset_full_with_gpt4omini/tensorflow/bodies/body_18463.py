# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs()
cond = pfor_input.stacked_input(0)
t = pfor_input.stacked_input(1)
e = pfor_input.stacked_input(2)
cond_rank = array_ops.rank(cond)
cond, t, e = smart_cond.smart_cond(
    cond_rank > 1, lambda: _inputs_with_flattening(pfor_input, [0, 1, 2]),
    lambda: [cond, t, e])
outputs = _create_op(
    pfor_input.op_type, [cond, t, e], [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
n = pfor_input.pfor.loop_len_vector
out = smart_cond.smart_cond(cond_rank > 1,
                            lambda: _unflatten_first_dim(outputs[0], n),
                            lambda: outputs[0])
exit([wrap(out, True) for x in outputs])
