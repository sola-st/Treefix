# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v1 = [
    variables_lib.Variable([1.]),
    variables_lib.Variable([2.]),
]
sv1 = sharded_variable.ShardedVariable(v1)
for v in sv1.variables:
    self.assertTrue(hasattr(v, '_sharded_container'))
    self.assertIs(v._sharded_container(), sv1)
