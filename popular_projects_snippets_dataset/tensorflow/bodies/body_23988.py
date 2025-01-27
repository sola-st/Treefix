# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = module.Module(name="simple")
self.assertEqual(mod.name, "simple")
self.assertEqual(mod.name_scope.name, "simple/")
