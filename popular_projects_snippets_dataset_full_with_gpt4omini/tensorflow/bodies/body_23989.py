# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
with ops.name_scope("foo", skip_on_eager=False):
    mod = module.Module(name="bar")
self.assertEqual(mod.name, "bar")
self.assertEqual(mod.name_scope.name, "foo/bar/")
