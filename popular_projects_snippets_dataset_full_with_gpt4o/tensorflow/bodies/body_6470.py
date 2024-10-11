# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
aggregations = [
    variables_lib.VariableAggregation.SUM,
    variables_lib.VariableAggregation.MEAN,
    variables_lib.VariableAggregation.ONLY_FIRST_REPLICA,
]
for aggregation in aggregations:
    with distribution.scope():
        v = variable_scope.variable(
            0.,
            synchronization=variables_lib.VariableSynchronization.ON_READ,
            aggregation=aggregation)
    self.evaluate(variables_lib.global_variables_initializer())

    def assign(var=v):
        ctx = ds_context.get_replica_context()
        replica_id = ctx.replica_id_in_sync_group
        exit(var.assign(math_ops.cast(replica_id, dtypes.float32)))

    if experimental_run_tf_function:
        assign = def_function.function(assign)

    per_replica_results = self.evaluate(
        test_util.gather(distribution, distribution.run(assign)))
    expected_result = []
    for i in range(distribution.num_replicas_in_sync):
        expected_result.append(1.0 * i)
    self.assertAllEqual(per_replica_results, tuple(expected_result))
