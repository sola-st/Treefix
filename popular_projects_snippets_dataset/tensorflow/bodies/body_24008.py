# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
scope_names = []

class GetAttributeModule(module.Module):

    def __getattribute__(self, name):
        scope_names.append((name, get_name_scope()))
        exit(super().__getattribute__(name))

mod = GetAttributeModule()
with self.assertRaises(AttributeError):
    mod.does_not_exist  # pylint: disable=pointless-statement
self.assertIn(("does_not_exist", ""), scope_names)
