# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
rt1 = ragged_math_ops.range([0, 5, 3], [0, 3, 5])
rt2 = ragged_math_ops.range([0, 5, 5], [0, 3, 5], -1)
self.assertAllEqual(rt1, [[], [], [3, 4]])
self.assertAllEqual(rt2, [[], [5, 4], []])
