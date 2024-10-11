# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
rt_as_list = [[0, 1, 2, 3], [4], [], [5, 6], [7], [8, 9]]
expected = (
    np.array([0 + 1 + 2 + 3, 4, 0, 5 + 6, 7, 8 + 9]) /
    np.array([4, 1, 0, 2, 1, 2]))
rt_input = ragged_factory_ops.constant(rt_as_list)
reduced = ragged_math_ops.reduce_mean(rt_input, axis=1)
self.assertEqualWithNan(self.evaluate(reduced), expected)
