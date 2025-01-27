# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v0 = variables_lib.Variable([0])
v1 = variables_lib.Variable([1])
s = sharded_variable.ShardedVariable([v0, v1], name='s')
self.assertEqual(s.variables[0], v0)
self.assertEqual(s.variables[1], v1)
self.assertEqual(s.shape.as_list(), [2])
self.assertEqual(s.dtype, v0.dtype)
self.assertEqual(s.name, 's')
