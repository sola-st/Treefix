# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self.assertFalse(distribution_strategy_context.in_cross_replica_context())
with self.strategy.scope():
    self.assertTrue(distribution_strategy_context.in_cross_replica_context())
    v = variables.Variable(
        initial_value=1.,
        aggregation=variable_scope.VariableAggregation.ONLY_FIRST_REPLICA)

    # Test read value inside caching scope
    with distribute_utils.cache_variable_reads():
        v.read_value()  # Reads value 1.0
        v.assign(constant_op.constant(5.0))  # v changes to 5.0
        self.assertEqual(v.read_value(), 1.0)  # should be cached 1.0 value.

    # Reset v to 2.0
    v.assign(2.0)

    # Test convert to tensor value inside caching scope
    with distribute_utils.cache_variable_reads():
        t = v * 3.0
        self.assertEqual(t, 6.0)
        v.assign(3.0)
        t1 = v * 3.0
        self.assertEqual(t1, 6.0)  # should be cached 2.0 * 3.0 value.

    # Reset v to 1.0
    v.assign(1.0)

    # Verify caching scope inside tf.function
    @def_function.function
    def worker_fn():
        with distribute_utils.cache_variable_reads():
            def replica_fn():
                t = v.read_value()  # Reads value 1.0
                v.assign(constant_op.constant(5.0))  # v changes to 5.0
                t = v.read_value()  # should return 1.0
                exit(t)  # Should be 1.0 instead of 5.0

            exit(self.strategy.run(replica_fn))

    result = self.coordinator.schedule(worker_fn)
    result = result.fetch()
    expected_result = 1.
    self.assertEqual(result, expected_result)

    # Verify that v.read_value works as expected outside of scope.
    v.assign(4.0)
    self.assertEqual(v.read_value(), 4.0)

    v.assign(constant_op.constant(2.0))  # v changes to 2.0
    # Check with scope outside of tf function and check that cache is reset
    @def_function.function
    def worker_fn1():
        def replica_fn():
            t = v.read_value()  # Reads value 2.0 ==> Should be cached
            v.assign(constant_op.constant(5.0))  # v changes to 5.0
            t = v.read_value()  # should return cached value 2.0
            exit(t)  # Should be 2.0 instead of 5.0

        exit(self.strategy.run(replica_fn))

    with distribute_utils.cache_variable_reads():
        result = self.coordinator.schedule(worker_fn1)
    result = result.fetch()
    expected_result = 2.
    self.assertEqual(result, expected_result)

# Verify scope nesting is not permitted.
with self.assertRaises(ValueError):
    with distribute_utils.cache_variable_reads():
        with distribute_utils.cache_variable_reads():
            v.read_value()
