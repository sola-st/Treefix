# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
self.assertAllEqual(
    ragged_math_ops.range([0, 3, 5], limits=0, deltas=-1),
    [list(range(0, 0, -1)),
     list(range(3, 0, -1)),
     list(range(5, 0, -1))])

self.assertAllEqual(
    ragged_math_ops.range([0, -3, 5], limits=0, deltas=[-1, 1, -2]),
    [list(range(0, 0, -1)),
     list(range(-3, 0, 1)),
     list(range(5, 0, -2))])
