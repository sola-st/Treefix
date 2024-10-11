# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
d, _, sess_config = self._get_test_objects(task_type, task_id, num_gpus)
num_shards = len(d.extended.parameter_devices)
partitioner = partitioned_variables.fixed_size_partitioner(num_shards)
with ops.Graph().as_default(), \
         self.cached_session(target=self._default_target,
                         config=sess_config) as sess, \
         d.scope():

    n = variable_scope.get_variable(
        'n',
        initializer=constant_op.constant([10.0, 20.0]),
        aggregation=variable_scope.VariableAggregation.SUM,
        partitioner=partitioner)

    for part_id, var in enumerate(n):
        self.assertEqual(var.device, '/job:ps/task:%d' % part_id)

    def model_fn():
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

    x = d.extended.call_for_each_replica(model_fn)

    if context.num_gpus() >= 1:
        self.evaluate(variables.global_variables_initializer())
        x_val = sess.run(x)
        if num_gpus < 1:
            self.assertEqual(x_val, [13.0, 25.0])
        else:
            x_expect = [10.0 + 3 * num_gpus, 20.0 + 5 * num_gpus]
            self.assertEqual(x_val, x_expect)
