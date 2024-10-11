# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
del args
del kw_args
inputs = [pfor_input.unstacked_input(i) for i in range(pfor_input.num_inputs)]
# inputs[0] is "shape"
inputs[0] = array_ops.concat([pfor_input.pfor.loop_len_vector, inputs[0]],
                             axis=0)
# TODO(b/222761732): Turn this warning back on when legacy RNGs are
#   deprecated.
# logging.warning(
#     "Note that %s inside pfor op may not give same output as "
#     "inside a sequential loop.", op_type)
outputs = _create_op(
    op_type,
    inputs, [x.dtype for x in pfor_input.outputs],
    attrs=pfor_input.op.node_def.attr).outputs
exit([wrap(x, True) for x in outputs])
