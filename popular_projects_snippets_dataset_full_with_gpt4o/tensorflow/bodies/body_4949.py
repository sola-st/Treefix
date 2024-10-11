# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
fname = os.path.join(self.get_temp_dir(), 'checkpoint')
model = autotrackable.AutoTrackable()
variables = [
    variables_lib.Variable([0]),
    variables_lib.Variable([1]),
    variables_lib.Variable([2]),
    variables_lib.Variable([3])
]
model.s = sharded_variable.ShardedVariable(variables)
cp = util.Checkpoint(model=model)
cp.write(fname)

model2 = autotrackable.AutoTrackable()
cp2 = util.Checkpoint(model=model2)
cp2.restore(fname)
variables2 = [
    variables_lib.Variable([0, 0]),
    variables_lib.Variable([0, 0])
]
model2.s = sharded_variable.ShardedVariable(variables2)
self.assertAllEqual(self.evaluate(model2.s.variables[0]), [0, 1])
self.assertAllEqual(self.evaluate(model2.s.variables[1]), [2, 3])
