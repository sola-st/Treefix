# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v1 = resource_variable_ops.ResourceVariable(1.)
v2 = resource_variable_ops.ResourceVariable(1.)
l = data_structures.ListWrapper([1, 2, v1, v2])
l[:] = 2, 8, 9, v2
self.assertEqual(l, [2, 8, 9, v2])
self.assertUnableToSave(l, "Unable to save .*__setslice__")
