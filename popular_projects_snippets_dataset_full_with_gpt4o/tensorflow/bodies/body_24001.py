# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
if context.executing_eagerly():
    self.skipTest("Graph specific")

mod = RecursiveModule(2)
self.assertEqual(mod.name_scope.name, "badger/")
self.assertEqual(mod.child.name_scope.name, "badger/badger/")

mod = RecursiveModule(2)
self.assertEqual(mod.name_scope.name, "badger_1/")
self.assertEqual(mod.child.name_scope.name, "badger_1/badger/")
