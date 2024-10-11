# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = ReturnsNameScopeModule()
for _ in range(3):
    self.assertEqual(mod(), mod.name_scope.name)
