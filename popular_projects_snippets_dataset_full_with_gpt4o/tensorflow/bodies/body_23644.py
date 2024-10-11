# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v1 = resource_variable_ops.ResourceVariable(1.)
v2 = resource_variable_ops.ResourceVariable(1.)

l1 = data_structures._TupleWrapper((v1, v2))
l2 = copy.copy(l1)
self.assertEqual(l1, (v1, v2))
self.assertEqual(l2, (v1, v2))
self.assertIs(l1[0], l2[0])
l2_deep = copy.deepcopy(l1)
self.assertIsNot(l1[0], l2_deep[0])
with self.assertRaises(AttributeError):
    l2.append(v1)
