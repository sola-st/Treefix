# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
variables = [
    variables_lib.Variable([0]),
    variables_lib.Variable([1]),
]
s = sharded_variable.ShardedVariable(variables)

got = nest.flatten(s)
self.assertIs(s, got[0])

got = nest.flatten(s, expand_composites=True)
expected = nest.flatten(variables, expand_composites=True)
self.assertEqual(got, expected)
