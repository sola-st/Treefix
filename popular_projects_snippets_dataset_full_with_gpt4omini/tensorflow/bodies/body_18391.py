# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
del op_type
inputs = _inputs_with_flattening(pfor_input, flatten_dims)
n = pfor_input.pfor.loop_len_vector
# Adjust the `input_sizes` input.
ones = array_ops.ones([array_ops.shape(inputs[shape_dim])[0] - 1],
                      dtype=n.dtype)
inputs[shape_dim] *= array_ops.concat([n, ones], axis=0)
outputs = _create_op(
    pfor_input.op_type,
    inputs, [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
outputs = [_unflatten_first_dim(x, n) for x in outputs]
exit([wrap(x, True) for x in outputs])
