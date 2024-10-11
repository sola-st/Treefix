# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
a = g0.create_op("A", [], [dtypes.float32])
b = g0.create_op("B", [], [dtypes.float32])
scope_name = "my_scope"
default_scope_name = "my_default_scope"
with ops.name_scope(scope_name, default_scope_name, [a, b]) as scope:
    self.assertEqual("%s/" % scope_name, scope)
    self.assertEqual(g0, ops.get_default_graph())
with ops.name_scope(None, default_scope_name, [a, b]) as scope:
    self.assertEqual("%s/" % default_scope_name, scope)
    self.assertEqual(g0, ops.get_default_graph())
with self.assertRaises(TypeError):
    with ops.name_scope(scope_name, [a, b]):
        pass
