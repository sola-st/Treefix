# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
self.assertEqual("foo", g.unique_name("foo"))
self.assertEqual("Foo_1", g.unique_name("Foo"))
with g.name_scope("bar"):
    self.assertEqual("bar/foo", g.unique_name("foo"))
with g.name_scope("Bar"):
    self.assertEqual("Bar_1/foo", g.unique_name("foo"))
