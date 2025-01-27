# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
x = ragged_factory_ops.constant([[3, 1, 4], [], [1, 5]])
y = ragged_factory_ops.constant([[[3, 1, 4], []], [], [[1, 5]]])
with self.assertRaisesRegex(
    ValueError, r'All ragged inputs must have the same ragged_rank.'):
    ragged_functional_ops.map_flat_values(math_ops.add, x, y)
