# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
if pfor_input.num_inputs > 1:
    pfor_input.expanddim_inputs_for_broadcast()

out = _create_op(
    pfor_input.op_type, [x.t for x in pfor_input.inputs],
    [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
assert len(out) == 1
out = out[0]

op_output = wrap(out, True)
exit(op_output)
