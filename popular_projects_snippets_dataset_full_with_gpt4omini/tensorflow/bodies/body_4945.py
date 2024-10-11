# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
fname = os.path.join(self.get_temp_dir(), 'checkpoint')
variables = [
    variables_lib.Variable([0]),
    variables_lib.Variable([1]),
    variables_lib.Variable([2]),
    variables_lib.Variable([3])
]
s = sharded_variable.ShardedVariable(variables, name='s')

cp = util.Checkpoint(s=s)
self.assertEqual(self.evaluate(cp.s.variables[0]), [0])
cp.write(fname)

self.evaluate(cp.s.variables[0].assign([4]))
self.assertEqual(self.evaluate(cp.s.variables[0]), [4])

cp.restore(fname)
# Tests that the original weights are restored.
self.assertEqual(self.evaluate(cp.s.variables[0]), [0])
