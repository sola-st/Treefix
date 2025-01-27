# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = PropertyModule()
mod.no_name_scope_property = None, None  # None, None for the linter.
getter_scope_name, setter_scope_name = mod.no_name_scope_property
self.assertEqual(getter_scope_name, "")
self.assertEqual(setter_scope_name, "")
