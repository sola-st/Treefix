# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
self.assertEqual("foo_2", g.unique_name("foo_2"))
self.assertEqual("foo", g.unique_name("foo"))
self.assertEqual("foo_1", g.unique_name("foo"))
self.assertEqual("foo_3", g.unique_name("foo"))
