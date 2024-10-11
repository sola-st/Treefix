# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v = resource_variable_ops.ResourceVariable([1.])
l = data_structures._TupleWrapper((v,))
self.assertEqual([], l.layers)
self.assertEqual([v], l.variables)
self.assertEqual([v], l.trainable_weights)
self.assertEqual([], l.non_trainable_variables)
