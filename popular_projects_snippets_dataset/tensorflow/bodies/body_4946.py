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

variables2 = [variables_lib.Variable([0, 0, 0, 0])]
s2 = sharded_variable.ShardedVariable(variables2, name='s')

# Restore from 4 partitions into 1.
cp2 = util.Checkpoint(s=s2)
cp2.restore(fname)
self.assertAllEqual(self.evaluate(cp2.s.variables[0]), [0, 1, 2, 3])

self.evaluate(cp2.s.variables[0].assign([5, 10, 15, 20]))
cp2.write(fname)

# Restore 1 partition into 4.
cp.restore(fname)
self.assertEqual(self.evaluate(cp.s.variables[0]), [5])
self.assertEqual(self.evaluate(cp.s.variables[1]), [10])
self.assertEqual(self.evaluate(cp.s.variables[2]), [15])
self.assertEqual(self.evaluate(cp.s.variables[3]), [20])
