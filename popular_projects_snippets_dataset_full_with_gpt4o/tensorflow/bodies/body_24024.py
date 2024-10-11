# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
m = TreeModule()
leaf1 = m.new_leaf()
self.assertEqual(set(m.submodules), {leaf1})
leaf2 = m.new_leaf()
self.assertEqual(set(m.submodules), {leaf1, leaf2})
