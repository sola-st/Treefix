# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
# Specify limits only.
self.assertAllEqual(
    ragged_math_ops.range([0, 3, 5]),
    [list(range(0)), list(range(3)),
     list(range(5))])

# Specify starts and limits.
self.assertAllEqual(
    ragged_math_ops.range([0, 3, 5], [2, 3, 10]),
    [list(range(0, 2)),
     list(range(3, 3)),
     list(range(5, 10))])

# Specify starts, limits, and deltas.
self.assertAllEqual(
    ragged_math_ops.range([0, 3, 5], [4, 4, 15], [2, 3, 4]),
    [list(range(0, 4, 2)),
     list(range(3, 4, 3)),
     list(range(5, 15, 4))])
