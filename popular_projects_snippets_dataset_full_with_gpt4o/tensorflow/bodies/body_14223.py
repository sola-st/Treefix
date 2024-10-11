# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector_test.py
"""Test for make_list_of_t."""
g0 = ops_lib.Graph()
with g0.as_default():
    a0 = constant_op.constant(1)
    b0 = constant_op.constant(2)
    c0 = math_ops.add(a0, b0)  # pylint: disable=unused-variable
# Should extract the tensors from the graph.
self.assertEqual(len(op_selector.make_list_of_t(g0)), 3)
# Should extract the tensors from the tuple
self.assertEqual(len(op_selector.make_list_of_t((a0, b0))), 2)
# Should extract the tensors and ignore the ops.
self.assertEqual(
    len(op_selector.make_list_of_t(
        (a0, a0.op, b0), ignore_ops=True)), 2)
