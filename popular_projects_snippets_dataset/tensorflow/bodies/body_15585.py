# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
"""Test the examples in apply_op_to_ragged_values.__doc__."""
rt = ragged_factory_ops.constant([[1, 2, 3], [], [4, 5], [6]])
v1 = ragged_functional_ops.map_flat_values(array_ops.ones_like, rt)
v2 = ragged_functional_ops.map_flat_values(math_ops.multiply, rt, rt)
v3 = ragged_functional_ops.map_flat_values(math_ops.add, rt, 5)
self.assertAllEqual(v1, [[1, 1, 1], [], [1, 1], [1]])
self.assertAllEqual(v2, [[1, 4, 9], [], [16, 25], [36]])
self.assertAllEqual(v3, [[6, 7, 8], [], [9, 10], [11]])
