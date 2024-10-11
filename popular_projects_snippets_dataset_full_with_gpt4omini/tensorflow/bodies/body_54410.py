# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
scope_name = "my_scope"
with ops.name_scope(scope_name, values=graph_elements) as scope:
    self.assertEqual("%s/" % scope_name, scope)
    self.assertEqual(graph_elements[0].graph, ops.get_default_graph())
g1 = ops.Graph()
a = g1.create_op("A", [], [dtypes.float32])
with self.assertRaises(ValueError):
    with ops.name_scope(scope_name, values=graph_elements + [a]):
        pass
