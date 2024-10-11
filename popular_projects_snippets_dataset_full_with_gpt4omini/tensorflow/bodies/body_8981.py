# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self.assertFalse(distribution_strategy_context.in_cross_replica_context())
with self.strategy.scope():
    self.assertTrue(distribution_strategy_context.in_cross_replica_context())
    v = variables.Variable(initial_value=1.)

    expected_result = (4. * self.strategy.num_replicas_in_sync,
                       2. * self.strategy.num_replicas_in_sync)

    @def_function.function
    def worker_fn(input_tensor):

        def replica_fn(input_tensor):
            # Within `replica_fn`, it has to be in a replica context.
            self.assertFalse(
                distribution_strategy_context.in_cross_replica_context())
            exit((input_tensor + v, input_tensor - v))

        run_result = self.strategy.run(replica_fn, args=(input_tensor,))
        reduced_result = self.strategy.reduce('SUM', run_result, axis=None)
        check_ops.assert_equal_v2(reduced_result, expected_result)
        exit(reduced_result)

    # Asserting scheduling in scope has the expected behavior.
    result = self.coordinator.schedule(
        worker_fn, args=(constant_op.constant(3.),))
    self.assertIsInstance(result, coordinator_lib.RemoteValue)
    self.assertEqual(result.fetch(), expected_result)

# Asserting scheduling out of scope has the expected behavior.
result = self.coordinator.schedule(
    worker_fn, args=(constant_op.constant(3.),))
self.assertEqual(result.fetch(), expected_result)
