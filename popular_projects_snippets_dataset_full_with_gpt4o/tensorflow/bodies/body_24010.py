# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
if tf2.enabled():
    self.skipTest("Requires TF1")

mod = module.Module(name="name")
name_scope_1 = mod.name_scope
name_scope_2 = mod.name_scope
self.assertIsNot(name_scope_1, name_scope_2)
self.assertEqual(name_scope_1.name, name_scope_2.name)
