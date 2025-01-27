# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
m = RecursiveModule(3)
self.assertEqual(m.trainable_variables,
                 (m.w, m.child.w, m.child.child.w))
self.assertEqual(m.child.trainable_variables,
                 (m.child.w, m.child.child.w))
self.assertEqual(m.child.child.trainable_variables, (m.child.child.w,))
