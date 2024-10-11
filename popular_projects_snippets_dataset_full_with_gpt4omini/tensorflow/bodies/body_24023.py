# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
m = RecursiveModule(3)
self.assertEqual(list(m.submodules), [m.child, m.child.child])
self.assertEqual(list(m.child.submodules), [m.child.child])
self.assertEqual(list(m.child.child.submodules), [])
