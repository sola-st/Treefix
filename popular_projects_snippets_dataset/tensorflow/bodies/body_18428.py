# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# TODO(jmenick): Add support for unstacked params.
pfor_input.stack_inputs(stack_indices=[1])
params = pfor_input.stacked_input(0)
indices = pfor_input.stacked_input(1)
stacked_result = array_ops.gather_nd(params, indices, batch_dims=1)
exit(wrap(stacked_result, True))
