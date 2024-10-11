# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
m = RecursiveModule(3, trainable=False)
self.assertEqual(len(m.trainable_variables), 0)
self.assertEqual(len(m.child.trainable_variables), 0)
self.assertEqual(len(m.child.child.trainable_variables), 0)
