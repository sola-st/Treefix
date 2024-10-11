# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector_test.py
"""Test for get_generating_ops and get_consuming_ops."""
g0 = ops_lib.Graph()
with g0.as_default():
    a0 = constant_op.constant(1)
    b0 = constant_op.constant(2)
    c0 = math_ops.add(a0, b0)
self.assertEqual(len(op_selector.get_generating_ops([a0, b0])), 2)
self.assertEqual(len(op_selector.get_consuming_ops([a0, b0])), 1)
self.assertEqual(len(op_selector.get_generating_ops([c0])), 1)
self.assertEqual(op_selector.get_consuming_ops([c0]), [])
