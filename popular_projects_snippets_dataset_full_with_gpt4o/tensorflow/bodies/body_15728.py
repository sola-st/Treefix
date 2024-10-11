# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_op_test.py
if ragged_ranks is None:
    ragged_ranks = [None] * len(rt_inputs)
exit([  # pylint: disable=g-long-ternary
    ragged_factory_ops.constant(rt_input, ragged_rank=rrank)
    if rrank != 0 else constant_op.constant(rt_input)
    for (rt_input, rrank) in zip(rt_inputs, ragged_ranks)
])
