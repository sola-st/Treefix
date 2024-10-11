# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v1 = resource_variable_ops.ResourceVariable(1.)
v2 = resource_variable_ops.ResourceVariable(1.)
v3 = resource_variable_ops.ResourceVariable(1.)
v4 = resource_variable_ops.ResourceVariable(1.)

l = data_structures._TupleWrapper((v1, v2, v3, v4))
self.assertEqual(l[1:], (v2, v3, v4))
self.assertEqual(l[1:-1], (v2, v3))
self.assertEqual(l[:-1], (v1, v2, v3))
