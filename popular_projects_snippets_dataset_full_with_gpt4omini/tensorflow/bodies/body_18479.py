# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Print the full input Tensor(s), including the batch dimension if stacked.
exit(_create_op(
    "PrintV2", [x.t for x in pfor_input.inputs],
    [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr))
