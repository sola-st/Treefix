# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.name_scope("foo", skip_on_eager=False) as foo:
    self.assertEqual("foo/", foo)
    with ops.name_scope("foo2", skip_on_eager=False) as foo2:
        self.assertEqual("foo/foo2/", foo2)
    with ops.name_scope(None, skip_on_eager=False) as empty1:
        self.assertEqual("", empty1)
        with ops.name_scope("foo3", skip_on_eager=False) as foo3:
            self.assertEqual("foo3/", foo3)
    with ops.name_scope("", skip_on_eager=False) as empty2:
        self.assertEqual("", empty2)
with ops.name_scope("foo/", skip_on_eager=False) as outer_foo:
    self.assertEqual("foo/", outer_foo)
    with ops.name_scope("", skip_on_eager=False) as empty3:
        self.assertEqual("", empty3)
    with ops.name_scope("foo4", skip_on_eager=False) as foo4:
        self.assertEqual("foo/foo4/", foo4)
    with ops.name_scope("foo5//", skip_on_eager=False) as foo5:
        self.assertEqual("foo5//", foo5)
        with ops.name_scope("foo6", skip_on_eager=False) as foo6:
            self.assertEqual("foo5//foo6/", foo6)
    with ops.name_scope("/", skip_on_eager=False) as foo7:
        self.assertEqual("/", foo7)
    with ops.name_scope("//", skip_on_eager=False) as foo8:
        self.assertEqual("//", foo8)
    with ops.name_scope("a//b/c", skip_on_eager=False) as foo9:
        self.assertEqual("foo/a//b/c/", foo9)
with ops.name_scope("a//b/c", skip_on_eager=False) as foo10:
    self.assertEqual("a//b/c/", foo10)
