# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_stack_op_test.py
if ragged_ranks is None:
    ragged_ranks = [None] * len(rt_inputs)
rt_inputs = [
    ragged_factory_ops.constant(rt_input, ragged_rank=rrank)  # pylint: disable=g-long-ternary
    if rrank != 0 else constant_op.constant(rt_input)
    for (rt_input, rrank) in zip(rt_inputs, ragged_ranks)
]
stacked = ragged_concat_ops.stack(rt_inputs, axis)
if expected_ragged_rank is not None:
    self.assertEqual(stacked.ragged_rank, expected_ragged_rank)
if expected_shape is not None:
    self.assertEqual(stacked.shape.as_list(), expected_shape)
self.assertAllEqual(stacked, expected)
