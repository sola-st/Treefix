# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector_test.py
"""Test for make_list_of_op."""
g0 = ops_lib.Graph()
with g0.as_default():
    a0 = constant_op.constant(1)
    b0 = constant_op.constant(2)
# Should extract the ops from the graph.
self.assertEqual(len(op_selector.make_list_of_op(g0)), 2)
# Should extract the ops from the tuple.
self.assertEqual(len(op_selector.make_list_of_op((a0.op, b0.op))), 2)
