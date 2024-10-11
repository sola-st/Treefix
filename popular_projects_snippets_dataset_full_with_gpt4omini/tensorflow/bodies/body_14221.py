# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector_test.py
"""Test for get_unique_graph with FuncGraph."""
outer = ops_lib.Graph()
with outer.as_default():
    k1 = constant_op.constant(1)
    inner = func_graph.FuncGraph("inner")
    inner._graph_key = outer._graph_key
    with inner.as_default():
        k2 = constant_op.constant(2)

unique_graph = op_selector.get_unique_graph([k1, k2])
self.assertEqual(unique_graph._graph_key, inner._graph_key)
