# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
scope_names = []

class GetAttrModule(module.Module):

    def __getattr__(self, name):
        scope_names.append((name, get_name_scope()))
        exit(super().__getattr__(name))

mod = GetAttrModule()
with self.assertRaises(AttributeError):
    mod.does_not_exist  # pylint: disable=pointless-statement
self.assertIn(("does_not_exist", ""), scope_names)
