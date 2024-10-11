# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
# ragged_rank=0
x0 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
y0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
self.assertAllEqual(
    math_ops.multiply(x0, y0), [3, 2, 12, 4, 25, 54, 14, 48, 45])

# ragged_rank=1
x1 = ragged_factory_ops.constant([[3, 1, 4], [], [1, 5], [9, 2], [6, 5]])
y1 = ragged_factory_ops.constant([[1, 2, 3], [], [4, 5], [6, 7], [8, 9]])
self.assertRaggedMapInnerValuesReturns(
    op=math_ops.multiply,
    args=(x1, y1),
    expected=[[3, 2, 12], [], [4, 25], [54, 14], [48, 45]])

# ragged_rank=2
x2 = ragged_factory_ops.constant([[[3, 1, 4]], [], [[], [1, 5]],
                                  [[9, 2], [6, 5]]])
y2 = ragged_factory_ops.constant([[[1, 2, 3]], [], [[], [4, 5]],
                                  [[6, 7], [8, 9]]])
self.assertRaggedMapInnerValuesReturns(
    op=math_ops.multiply,
    args=(x2, y2),
    expected=[[[3, 2, 12]],          # row 0
              [],                    # row 1
              [[], [4, 25]],         # row 2
              [[54, 14], [48, 45]]   # row 3
             ])  # pyformat: disable

# ragged_rank=3
x3 = ragged_factory_ops.constant([[[[3, 1, 4]], []], [], [[[], [1, 5]]],
                                  [[[9, 2], [6, 5]]]])
y3 = ragged_factory_ops.constant([[[[1, 2, 3]], []], [], [[[], [4, 5]]],
                                  [[[6, 7], [8, 9]]]])
self.assertRaggedMapInnerValuesReturns(
    op=math_ops.multiply,
    args=(x3, y3),
    expected=[
        [[[3, 2, 12]], []],       # row 0
        [],                       # row 1
        [[[], [4, 25]]],          # row 2
        [[[54, 14], [48, 45]]]    # row 3
    ])  # pyformat: disable
