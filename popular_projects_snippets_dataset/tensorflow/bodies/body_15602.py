# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
"""Examples from ragged_range.__doc__."""
rt1 = ragged_math_ops.range([3, 5, 2])
self.assertAllEqual(rt1, [[0, 1, 2], [0, 1, 2, 3, 4], [0, 1]])

rt2 = ragged_math_ops.range([0, 5, 8], [3, 3, 12])
self.assertAllEqual(rt2, [[0, 1, 2], [], [8, 9, 10, 11]])

rt3 = ragged_math_ops.range([0, 5, 8], [3, 3, 12], 2)
self.assertAllEqual(rt3, [[0, 2], [], [8, 10]])
