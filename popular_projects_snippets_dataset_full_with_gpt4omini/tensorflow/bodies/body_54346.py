# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()

with g.name_scope("foo") as foo:
    self.assertEqual("foo/", foo)
    with g.name_scope("foo2") as foo2:
        self.assertEqual("foo/foo2/", foo2)
    with g.name_scope(None) as empty1:
        self.assertEqual("", empty1)
        with g.name_scope("foo3") as foo3:
            self.assertEqual("foo3/", foo3)
    with g.name_scope("") as empty2:
        self.assertEqual("", empty2)

self.assertEqual("FloatOutput",
                 g.create_op("FloatOutput", [], [dtypes.float32]).name)
with g.name_scope("bar") as scope:
    self.assertEqual("bar/FloatOutput",
                     g.create_op("FloatOutput", [], [dtypes.float32]).name)
    self.assertEqual("bar/FloatOutput_1",
                     g.create_op("FloatOutput", [], [dtypes.float32]).name)
    # If you use the value from "with .. as", that values is used as-is.
    self.assertEqual(
        "bar", g.create_op(
            "FloatOutput", [], [dtypes.float32], name=scope).name)
with g.name_scope("baz") as scope:
    with g.name_scope("quux"):
        self.assertEqual("baz/quux/FloatOutput",
                         g.create_op("FloatOutput", [], [dtypes.float32]).name)
    # If you use the value from the enclosing "with .. as", nothing is pushed.
    with g.name_scope(scope):
        self.assertEqual("baz/FloatOutput",
                         g.create_op("FloatOutput", [], [dtypes.float32]).name)
        self.assertEqual(
            "baz", g.create_op(
                "FloatOutput", [], [dtypes.float32], name=scope).name)
        self.assertEqual(
            "trailing",
            g.create_op(
                "FloatOutput", [], [dtypes.float32], name="trailing/").name)
with g.name_scope("bar"):
    self.assertEqual("bar_1/FloatOutput",
                     g.create_op("FloatOutput", [], [dtypes.float32]).name)
with g.name_scope("bar/"):
    self.assertEqual("bar/FloatOutput_2",
                     g.create_op("FloatOutput", [], [dtypes.float32]).name)
