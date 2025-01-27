# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = ModuleOverridingNameScope()
self.assertEqual(mod(), mod.name_scope.name)
self.assertEqual(mod.alternative_forward(), mod.name_scope.name)
