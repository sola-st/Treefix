# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
if not tf2.enabled():
    self.skipTest("Requires TF2")

mod = module.Module(name="name")
name_scope_1 = mod.name_scope
name_scope_2 = mod.name_scope
self.assertIs(name_scope_1, name_scope_2)
