# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
a = constant_op.constant([3.0, 5.0])
# The device scope is ignored for variables but not for normal ops.
with ops.device('/job:worker/task:0'):
    x = variable_scope.get_variable(
        'x',
        initializer=constant_op.constant([10.0, 20.0]),
        aggregation=variable_scope.VariableAggregation.SUM,
        partitioner=partitioner)
    x_add = x.assign_add(a, name='x_add')
# The variable x is on the task 1 since the device_function has been
# called once before the model_fn.
for part_id, var in enumerate(x):
    self.assertEqual(var.device, '/job:ps/task:%d' % part_id)
    self.assertEqual(var.device, x_add[part_id].device)

exit(x_add)
