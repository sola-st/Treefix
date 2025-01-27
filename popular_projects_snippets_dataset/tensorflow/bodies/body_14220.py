# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector_test.py
"""Test for check_graphs and get_unique_graph."""
g0 = ops_lib.Graph()
with g0.as_default():
    a0 = constant_op.constant(1)
    b0 = constant_op.constant(2)
g1 = ops_lib.Graph()
with g1.as_default():
    a1 = constant_op.constant(1)
    b1 = constant_op.constant(2)
# Same graph, should be fine.
self.assertIsNone(op_selector.check_graphs(a0, b0))
# Two different graphs, should assert.
with self.assertRaises(ValueError):
    op_selector.check_graphs(a0, b0, a1, b1)
# a0 and b0 belongs to the same graph, should be fine.
self.assertEqual(op_selector.get_unique_graph([a0, b0]), g0)
# Different graph, should raise an error.
with self.assertRaises(ValueError):
    op_selector.get_unique_graph([a0, b0, a1, b1])
