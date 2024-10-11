# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
super().__init__()
variables = [
    variables_lib.Variable([0]),
    variables_lib.Variable([1]),
]
self.w = sharded_variable.ShardedVariable(variables)
