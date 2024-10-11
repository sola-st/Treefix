# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
condition = ragged_factory_ops.constant(
    [[True, True, False], [], [True, False]])  # pyformat: disable
x = ragged_factory_ops.constant([['a', 'b', 'c'], [], ['d', 'e']])
y = ragged_factory_ops.constant([['A', 'B', 'C'], [], ['D', 'E']])
self.assertRaggedMapInnerValuesReturns(
    op=array_ops.where_v2,
    args=(condition, x, y),
    expected=[[b'a', b'b', b'C'], [], [b'd', b'E']])
