# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.name_scope(""):  # Should not raise
    pass
with g.name_scope("foo/"):  # Should not raise
    with g.name_scope("_bar"):  # Should not raise
        pass
with self.assertRaises(ValueError):
    with g.name_scope("foo:0"):
        pass
with self.assertRaises(ValueError):
    with g.name_scope("_bar"):
        pass
