# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
y = ragged_factory_ops.constant([[1, 2, 3], [], [4, 5]])
self.assertRaggedMapInnerValuesReturns(
    op=math_ops.multiply, args=(5, y), expected=[[5, 10, 15], [], [20, 25]])
