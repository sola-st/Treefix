# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v = resource_variable_ops.ResourceVariable(1.)
l = data_structures.List([v])
l *= 2
self.assertEqual(list(l), [v] * 2)
