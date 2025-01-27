# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
foo = ops.name_scope_v2("foo")
bar = ops.name_scope_v2("bar")
with foo as scope_name:
    self.assertEqual("foo/", scope_name)
    with foo as scope_name:
        self.assertEqual("foo/foo/", scope_name)
    with bar as scope_name:
        self.assertEqual("foo/bar/", scope_name)
        with foo as scope_name:
            self.assertEqual("foo/bar/foo/", scope_name)
with bar as scope_name:
    self.assertEqual("bar/", scope_name)
