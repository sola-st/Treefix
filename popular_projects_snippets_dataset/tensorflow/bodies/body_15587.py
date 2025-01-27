# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
x = ragged_factory_ops.constant([[3, 1, 4], [], [1, 5]])
y = ragged_factory_ops.constant([[1, 2, 3], [], [4, 5]])
self.assertRaggedMapInnerValuesReturns(
    op=math_ops.multiply, args=(x, y), expected=[[3, 2, 12], [], [4, 25]])
