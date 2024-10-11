# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
if not context.executing_eagerly():
    self.skipTest("Eager specific")

mod = RecursiveModule(2)
self.assertEqual(mod.name_scope.name, "badger/")
self.assertEqual(mod.child.name_scope.name, "badger/badger/")

mod = RecursiveModule(2)
self.assertEqual(mod.name_scope.name, "badger/")
self.assertEqual(mod.child.name_scope.name, "badger/badger/")
