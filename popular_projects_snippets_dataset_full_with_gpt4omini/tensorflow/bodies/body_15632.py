# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
rt_as_list = [[0, 1, 1, 0], [4], [], [5, 6], [7], [8, 9]]
expected = ([std(0, 1, 1, 0), std(4), std(), std(5, 6), std(7), std(8, 9)])
rt_input = ragged_factory_ops.constant(rt_as_list)
reduced = ragged_math_ops.reduce_std(rt_input, axis=1)
self.assertEqualWithNan(self.evaluate(reduced), expected)
