# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
self.assertEqual("", g.get_name_scope())
with g.name_scope("") as scope:
    self.assertEqual("", scope)
    self.assertEqual("", g.get_name_scope())
with g.name_scope(None) as scope:
    self.assertEqual("", scope)
    self.assertEqual("", g.get_name_scope())
with g.name_scope("foo") as scope:
    self.assertEqual("foo/", scope)
    self.assertEqual("foo", g.get_name_scope())
    with g.name_scope("") as scope:
        self.assertEqual("", scope)
        self.assertEqual("", g.get_name_scope())
    with g.name_scope(None) as scope:
        self.assertEqual("", scope)
        self.assertEqual("", g.get_name_scope())
