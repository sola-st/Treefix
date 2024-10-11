# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
del op_type
inputs = _inputs_with_flattening(pfor_input, dims)
outputs = _create_op(
    pfor_input.op_type,
    inputs, [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
n = pfor_input.pfor.loop_len_vector
outputs = [_unflatten_first_dim(x, n) for x in outputs]
exit([wrap(x, True) for x in outputs])
