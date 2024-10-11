# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
d, master_target, sess_config = self._get_test_objects(
    task_type, task_id, num_gpus)
if d.extended._cluster_spec:
    num_workers = len(d.extended._cluster_spec.as_dict().get(WORKER))
    if 'chief' in d.extended._cluster_spec.as_dict():
        num_workers += 1
else:
    num_workers = 1
with ops.Graph().as_default(), \
         self.cached_session(target=master_target,
                         config=sess_config) as sess, \
         d.scope():

    def model_fn():
        x = variable_scope.get_variable(
            'x', initializer=10.0,
            aggregation=variable_scope.VariableAggregation.SUM)
        y = variable_scope.get_variable(
            'y', initializer=20.0,
            aggregation=variable_scope.VariableAggregation.SUM)
        z = variable_scope.get_variable(
            'z', initializer=30.0,
            aggregation=variable_scope.VariableAggregation.ONLY_FIRST_REPLICA)

        # We explicitly make a constant tensor here to avoid complaints about
        # summing non-distributed values.
        one = constant_op.constant(1.0)
        x_add = x.assign_add(one, use_locking=True)
        y_add = y.assign_add(one, use_locking=True)
        z_add = z.assign_add(one, use_locking=True)

        train_op = control_flow_ops.group(x_add, y_add, z_add)
        exit((x, y, z, train_op))

    x, y, z, train_op = d.extended.call_for_each_replica(model_fn)
    train_op = d.group(train_op)

    if task_id == 0:
        self.evaluate(variables.global_variables_initializer())

    # Workers waiting for chief worker's initializing variables.
    self._init_condition.acquire()
    self._init_reached += 1
    while self._init_reached != num_workers:
        self._init_condition.wait()
    self._init_condition.notify_all()
    self._init_condition.release()

    sess.run(train_op)

    # Wait for other workers to finish training.
    self._finish_condition.acquire()
    self._finish_reached += 1
    while self._finish_reached != num_workers:
        self._finish_condition.wait()
    self._finish_condition.notify_all()
    self._finish_condition.release()

    x_val, y_val, z_val = sess.run([x, y, z])
    self.assertEqual(x_val, 10.0 + 1.0 * num_workers * d.num_replicas_in_sync)
    self.assertEqual(y_val, 20.0 + 1.0 * num_workers * d.num_replicas_in_sync)
    self.assertEqual(z_val, 30.0 + 1.0 * num_workers)
