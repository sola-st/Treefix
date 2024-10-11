# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/per_replica_test.py
f = def_function.function(lambda x: x)
x = values_lib.PerReplica((constant_op.constant(1.),))
y = f(x)
self.assertIsNot(x, y)
nest.map_structure(self.assertAllEqual, x, y, expand_composites=True)
self.assertEqual(x._type_spec, y._type_spec)
