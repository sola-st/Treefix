# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
m = RecursiveModule(3)
self.assertEqual(m.variables, (m.w, m.child.w, m.child.child.w))
self.assertEqual(m.child.variables, (m.child.w, m.child.child.w))
self.assertEqual(m.child.child.variables, (m.child.child.w,))
