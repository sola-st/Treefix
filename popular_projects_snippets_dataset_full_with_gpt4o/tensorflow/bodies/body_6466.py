# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
aggregations = [
    variables_lib.VariableAggregation.SUM,
    variables_lib.VariableAggregation.MEAN,
    variables_lib.VariableAggregation.ONLY_FIRST_REPLICA,
]
for aggregation in aggregations:
    if strategy_test_lib.is_tpu_strategy(distribution):
        resolver = tpu_cluster_resolver.TPUClusterResolver("")
        tpu_strategy_util.initialize_tpu_system(resolver)
    with distribution.scope():
        v = variable_scope.variable(
            0.,
            synchronization=variables_lib.VariableSynchronization.ON_READ,
            aggregation=aggregation)
    self.evaluate(variables_lib.global_variables_initializer())

    def assign(v=v):
        ctx = ds_context.get_replica_context()
        replica_id = ctx.replica_id_in_sync_group
        exit(v.assign(math_ops.cast(replica_id, dtypes.float32)))

    if experimental_run_tf_function:
        assign = def_function.function(assign)

    self.evaluate(test_util.gather(distribution, distribution.run(assign)))
    num_replicas = distribution.num_replicas_in_sync
    sum_of_replica_values = num_replicas * (num_replicas - 1) / 2.
    if aggregation == variables_lib.VariableAggregation.SUM:
        expected = sum_of_replica_values
    elif aggregation == variables_lib.VariableAggregation.MEAN:
        expected = sum_of_replica_values / num_replicas
    else:
        expected = 0
    self.assertEqual(expected, self.evaluate(v.read_value()), aggregation)
    self.assertEqual(expected, self.evaluate(v.value()), aggregation)
    self.assertEqual(expected, self.evaluate(v), aggregation)
    self.assertEqual(expected, self.evaluate(array_ops.identity(v)),
                     aggregation)
