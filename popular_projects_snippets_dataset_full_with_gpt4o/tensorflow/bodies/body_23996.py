# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
with ops.name_scope("foo", skip_on_eager=False):
    mod = module.Module(name="bar")
mod.foo = get_name_scope
# `foo` is not a method so we do not re-enter the name scope.
self.assertEqual(mod.foo(), "")
