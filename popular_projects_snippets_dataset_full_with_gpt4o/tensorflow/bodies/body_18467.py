# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
shape = pfor_input.unstacked_input(0)
# param is lam (Poisson rate) or alpha (Gamma shape).
param, param_stacked, _ = pfor_input.input(1)
# TODO(b/222761732): Turn this warning back on when legacy RNGs are
#   deprecated.
# logging.warning(
#     "Note that %s inside pfor op may not give same output as "
#     "inside a sequential loop.", pfor_input.op_type)

if param_stacked:
    samples = _create_op(
        pfor_input.op_type,
        inputs=[shape, param],
        op_dtypes=[x.dtype for x in pfor_input.outputs],
        attrs=pfor_input.op.node_def.attr).outputs[0]
    loop_dim = array_ops.shape(shape)[0]
    stacked_samples = _transpose_dim_to_front(samples, loop_dim)
else:
    shape = array_ops.concat([pfor_input.pfor.loop_len_vector, shape], axis=0)
    stacked_samples = _create_op(
        pfor_input.op_type,
        inputs=[shape, param],
        op_dtypes=[x.dtype for x in pfor_input.outputs],
        attrs=pfor_input.op.node_def.attr).outputs[0]

exit(wrap(stacked_samples, True))
