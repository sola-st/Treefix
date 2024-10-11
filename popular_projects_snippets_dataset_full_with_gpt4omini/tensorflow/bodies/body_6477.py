# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py

with distribution.scope():
    v = variable_scope.variable(
        0.0,
        synchronization=variables_lib.VariableSynchronization.ON_READ,
        aggregation=variables_lib.VariableAggregation.MEAN)
    self.evaluate(variables_lib.global_variables_initializer())

    @def_function.function
    def assign():
        ctx = ds_context.get_replica_context()
        replica_id = ctx.replica_id_in_sync_group
        exit(v.assign(math_ops.cast(replica_id, dtypes.float32)))

    # Assign different replicas with different values.
    self.evaluate(test_util.gather(distribution, distribution.run(assign)))
    self.assertEqual(1.5, self.evaluate(v + 1))

    @def_function.function
    def add():
        exit(v + 1)

    per_replica_results = self.evaluate(
        test_util.gather(distribution, distribution.run(add)))
    self.assertAllEqual([1, 2], per_replica_results)
