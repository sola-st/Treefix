# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
x = constant_op.constant([[1, 2], [3, 4], [5, 6]])
y = constant_op.constant(2)
self.assertRaggedMapInnerValuesReturns(
    op=math_ops.multiply, args=(x, y), expected=[[2, 4], [6, 8], [10, 12]])
