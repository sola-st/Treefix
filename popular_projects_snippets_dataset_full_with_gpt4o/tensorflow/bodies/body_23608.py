# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
m = module.Module()
m.l = [1, 2]
m.l.insert(0, 0)
self.assertEqual(m.l, [0, 1, 2])
self.assertEqual(m.l._trackable_children(), {})
