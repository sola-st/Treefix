# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
n = pfor_input.num_inputs
pfor_input.stack_inputs(stack_indices=range(n - 1))
axis = pfor_input.unstacked_input(n - 1)
axis += math_ops.cast(axis >= 0, axis.dtype)
exit(wrap(
    array_ops.concat([x.t for x in pfor_input.inputs[:n - 1]], axis=axis),
    True))
