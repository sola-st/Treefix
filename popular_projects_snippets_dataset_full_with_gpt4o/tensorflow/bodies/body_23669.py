# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
m = module.Module()
m.s = (m,)
self.assertLen(m._trackable_children(), 1)
self.assertIn("s", m._trackable_children())
self.assertIs(m.s, m._trackable_children()["s"])
self.assertEqual((), m.trainable_variables)
