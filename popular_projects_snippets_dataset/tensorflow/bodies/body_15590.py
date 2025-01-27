# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
x = ragged_factory_ops.constant([[1, 2, 3], [], [4, 5]])
y = ragged_factory_ops.constant([[10, 20, 30], [], [40, 50]])
self.assertRaggedMapInnerValuesReturns(
    op=math_ops.add_n,
    args=([x, y, x],),
    expected=[[12, 24, 36], [], [48, 60]])
