# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v1 = resource_variable_ops.ResourceVariable(1.)
v2 = resource_variable_ops.ResourceVariable(1.)
v3 = resource_variable_ops.ResourceVariable(1.)

l1 = data_structures.List([v1, v2])
l2 = l1.copy()
l2.append(v3)
self.assertEqual(list(l1), [v1, v2])
self.assertEqual(list(l2), [v1, v2, v3])
