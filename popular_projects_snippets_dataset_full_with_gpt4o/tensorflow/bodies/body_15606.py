# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
# Specify starts and limits, broadcast deltas.
self.assertAllEqual(
    ragged_math_ops.range([0, 3, 5], [4, 4, 15], 3),
    [list(range(0, 4, 3)),
     list(range(3, 4, 3)),
     list(range(5, 15, 3))])

# Broadcast all arguments.
self.assertAllEqual(ragged_math_ops.range(0, 5, 1), [list(range(0, 5, 1))])
