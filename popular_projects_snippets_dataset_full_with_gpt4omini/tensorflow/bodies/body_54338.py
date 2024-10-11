# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
self.assertEqual("foo", g.unique_name("foo", mark_as_used=False))
self.assertEqual("foo", g.unique_name("foo", mark_as_used=False))
self.assertEqual("foo", g.unique_name("foo"))
self.assertEqual("foo_1", g.unique_name("foo", mark_as_used=False))
self.assertEqual("foo_1", g.unique_name("foo"))
self.assertEqual("foo_2", g.unique_name("foo", mark_as_used=False))
self.assertEqual("foo_2", g.unique_name("foo"))
self.assertEqual("foo_1_1", g.unique_name("foo_1", mark_as_used=False))
self.assertEqual("foo_1_1", g.unique_name("foo_1"))
self.assertEqual("foo_1_2", g.unique_name("foo_1", mark_as_used=False))
self.assertEqual("foo_1_2", g.unique_name("foo_1"))
self.assertEqual("foo_1_2_1", g.unique_name("foo_1_2", mark_as_used=False))
self.assertEqual("foo_1_2_1", g.unique_name("foo_1_2"))
with g.name_scope("bar"):
    self.assertEqual("bar/foo", g.unique_name("foo", mark_as_used=False))
    self.assertEqual("bar/foo", g.unique_name("foo"))
    self.assertEqual("bar/foo_1", g.unique_name("foo", mark_as_used=False))
    self.assertEqual("bar/foo_1", g.unique_name("foo"))
    with g.name_scope(None):
        self.assertEqual("foo_3", g.unique_name("foo", mark_as_used=False))
        self.assertEqual("foo_3", g.unique_name("foo"))
    with g.name_scope("baz"):
        self.assertEqual(
            "bar/baz/foo", g.unique_name(
                "foo", mark_as_used=False))
        self.assertEqual("bar/baz/foo", g.unique_name("foo"))
        self.assertEqual(
            "bar/baz/foo_1", g.unique_name(
                "foo", mark_as_used=False))
        self.assertEqual("bar/baz/foo_1", g.unique_name("foo"))
    with g.name_scope("baz"):
        self.assertEqual(
            "bar/baz_1/foo", g.unique_name(
                "foo", mark_as_used=False))
        self.assertEqual("bar/baz_1/foo", g.unique_name("foo"))
        self.assertEqual(
            "bar/baz_1/foo_1", g.unique_name(
                "foo", mark_as_used=False))
        self.assertEqual("bar/baz_1/foo_1", g.unique_name("foo"))
with g.name_scope("quux"):
    self.assertEqual("quux/foo", g.unique_name("foo", mark_as_used=False))
    self.assertEqual("quux/foo", g.unique_name("foo"))
with g.name_scope("bar"):
    with g.name_scope("baz"):
        self.assertEqual(
            "bar_1/baz/foo", g.unique_name(
                "foo", mark_as_used=False))
        self.assertEqual("bar_1/baz/foo", g.unique_name("foo"))
self.assertEqual("foo_4", g.unique_name("foo", mark_as_used=False))
self.assertEqual("foo_4", g.unique_name("foo"))
self.assertEqual("bar_2", g.unique_name("bar", mark_as_used=False))
self.assertEqual("bar_2", g.unique_name("bar"))
