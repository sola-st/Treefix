# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
rt_as_list = [[0, 1, 2, 3], [4], [], [5, 6], [7], [8, 9]]
expected = ([
    variance(0, 1, 2, 3),
    variance(4),
    variance(),
    variance(5, 6),
    variance(7),
    variance(8, 9)
])
rt_input = ragged_factory_ops.constant(rt_as_list)
reduced = ragged_math_ops.reduce_variance(rt_input, axis=1)
self.assertEqualWithNan(self.evaluate(reduced), expected)
