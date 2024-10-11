# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self.assertFalse(distribution_strategy_context.in_cross_replica_context())
with self.strategy.scope():
    self.assertTrue(distribution_strategy_context.in_cross_replica_context())
    v = variables.Variable(
        initial_value=1.,
        aggregation=variable_scope.VariableAggregation.SUM)

    @def_function.function
    def worker_fn():

        def replica_fn():
            value = math_ops.cast(
                distribution_strategy_context.get_replica_context()
                .replica_id_in_sync_group + 1, v.dtype)
            v.assign(value)

        self.strategy.run(replica_fn)

    self.coordinator.schedule(worker_fn)
    self.coordinator.join()
    expected_result = 0.
    for i in range(self.strategy.num_replicas_in_sync):
        expected_result = expected_result + i + 1
    self.assertEqual(v, expected_result)
