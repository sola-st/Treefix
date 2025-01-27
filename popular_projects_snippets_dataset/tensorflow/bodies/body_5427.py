# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
strategy.extended._allow_run_without_coordinator = True
with strategy.scope():
    v = variables.Variable(
        initial_value=[0, 0, 0, 0, 0, 0, 0, 0],
        dtype=dtypes.float32,
        aggregation=variable_scope.VariableAggregation.SUM)

if strategy.num_replicas_in_sync > 1:
    self.assertIsInstance(v, ps_values.AggregatingVariable)
else:
    self.assertIsInstance(v, variables.Variable)

def replica_fn():
    replica_id = distribution_strategy_context.get_replica_context(
    ).replica_id_in_sync_group
    val = array_ops.reshape(
        math_ops.cast(replica_id + 10, dtype=v.dtype), [1])
    v.assign(
        array_ops.concat(
            [val, constant_op.constant([1., 2., 3., 4., 5., 6., 7.])], 0))

strategy.run(replica_fn)

expected_result = np.arange(8.) * strategy.num_replicas_in_sync
for i in range(strategy.num_replicas_in_sync):
    expected_result[0] = expected_result[0] + i + 10
self.assertAllEqual(v, expected_result)
