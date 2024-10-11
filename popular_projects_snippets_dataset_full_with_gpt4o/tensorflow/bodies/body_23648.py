# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
# Note: tuple behavior differs from list behavior. Lists are mutated by
# imul/iadd, tuples assign a new object to the left hand side of the
# expression.
v = resource_variable_ops.ResourceVariable(1.)
l = data_structures._TupleWrapper((v,))
original = l
l *= 2
self.assertEqual(l, (v,) * 2)
self.assertNotEqual(original, (v,) * 2)
