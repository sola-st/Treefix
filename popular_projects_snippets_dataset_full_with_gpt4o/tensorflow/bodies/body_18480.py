# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Format using the full input Tensor(s), including the batch dimension if
# stacked.
op = _create_op(
    "StringFormat", [x.t for x in pfor_input.inputs],
    [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr)
exit([wrap(output, False) for output in op.outputs])
