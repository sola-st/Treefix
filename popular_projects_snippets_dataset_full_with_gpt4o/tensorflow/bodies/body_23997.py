# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = PropertyModule()
mod.some_property = None, None  # None, None for the linter.
getter_scope_name, setter_scope_name = mod.some_property
self.assertEqual(getter_scope_name, "property_module/")
self.assertEqual(setter_scope_name, "property_module/")
