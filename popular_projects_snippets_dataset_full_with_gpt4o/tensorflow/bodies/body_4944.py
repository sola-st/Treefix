# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v0 = variables_lib.Variable([[0, 0]])
v1 = variables_lib.Variable([[1, 1], [2, 2]])
v2 = variables_lib.Variable([[3, 3]])
s = sharded_variable.ShardedVariable([v0, v1, v2])
t = ops.convert_to_tensor(s)
self.assertAllEqual(t, [[0, 0], [1, 1], [2, 2], [3, 3]])
