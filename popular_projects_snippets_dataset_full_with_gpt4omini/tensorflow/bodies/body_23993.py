# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
m = TreeModule()
self.assertEqual(m.name, "tree_module")
self.assertEqual(m.name_scope.name, "tree_module/")
leaf1 = m.new_leaf()
self.assertEqual(leaf1.name, "tree_module")
self.assertEqual(leaf1.name_scope.name, "tree_module/tree_module/")
