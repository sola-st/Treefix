# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
del args
del kw_args
# TODO(agarwal): Looks like these ops don't support broadcasting. Hence we
# have to use tiling here.
pfor_input.stack_inputs()
outputs = _create_op(
    op_type, [x.t for x in pfor_input.inputs],
    [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
exit([wrap(x, True) for x in outputs])
