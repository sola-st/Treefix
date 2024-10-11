# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = RecursiveModule(3)
self.assertEqual(mod.w.name, "badger/mushroom:0")
self.assertEqual(mod.child.w.name, "badger/badger/mushroom:0")
self.assertEqual(mod.child.child.w.name, "badger/badger/badger/mushroom:0")
