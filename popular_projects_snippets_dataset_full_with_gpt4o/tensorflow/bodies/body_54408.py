# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
a = g0.create_op("A", [], [dtypes.float32])
b = g0.create_op("B", [], [dtypes.float32])
with ops.name_scope("", values=[a, b]) as scope:
    self.assertEqual("", scope)
    self.assertEqual(g0, ops.get_default_graph())
with ops.name_scope("", "my_default_scope", [a, b]) as scope:
    self.assertEqual("", scope)
    self.assertEqual(g0, ops.get_default_graph())
