# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v = resource_variable_ops.ResourceVariable([1.])
l = data_structures.List([v])
self.assertTrue(l.trainable)
self.assertEqual([], l.layers)
self.assertEqual([v], l.variables)
self.assertEqual([v], l.trainable_weights)
self.assertEqual([], l.non_trainable_variables)
l.trainable = False
self.assertEqual([v], l.variables)
self.assertEqual([], l.trainable_variables)
self.assertEqual([v], l.non_trainable_variables)
l.trainable = True
v2 = resource_variable_ops.ResourceVariable(1., trainable=False)
l.append(v2)
self.assertEqual([v, v2], l.weights)
self.assertEqual([v], l.trainable_weights)
self.assertEqual([v2], l.non_trainable_weights)
