# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v = resource_variable_ops.ResourceVariable(1.)
l = data_structures._TupleWrapper((v,))
original = l
l += (1,)
self.assertEqual(l, (v, 1))
self.assertNotEqual(original, (v, 1))
self.assertEqual(original, (v,))
