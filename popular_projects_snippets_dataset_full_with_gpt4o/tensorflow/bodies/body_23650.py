# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v = resource_variable_ops.ResourceVariable(1.)
l = data_structures._TupleWrapper((v, v, v))
self.assertEqual(l * 2, (v, v, v) * 2)
