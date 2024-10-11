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
cp.write(fname)

variables2 = [
    variables_lib.Variable([0, 0]),
    variables_lib.Variable([0, 0])
]
s2 = sharded_variable.ShardedVariable(variables2, name='s')
cp2 = util.Checkpoint(s=s2)
cp2.restore(fname)
# Assert that weights from the 4 partitions were loaded here.
self.assertLen(cp2.s.variables, 2)
self.assertAllEqual(self.evaluate(cp2.s.variables[0]), [0, 1])
self.assertAllEqual(self.evaluate(cp2.s.variables[1]), [2, 3])
