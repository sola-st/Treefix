# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v1 = [
    variables_lib.Variable([1.]),
    variables_lib.Variable([2.]),
]
sv1 = sharded_variable.ShardedVariable(v1)

v2 = [
    variables_lib.Variable([1.]),
    variables_lib.Variable([2.]),
]
sv2 = sharded_variable.ShardedVariable(v2)

equal = sv1 == sv2
self.assertAllEqual(equal, [True, True])
self.assertAllEqual(sv1 + sv2, [2.0, 4.0])
