# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
if isinstance(distribution.extended,
              collective_all_reduce_strategy.CollectiveAllReduceExtended):
    self.skipTest("b/212945803")
with distribution.scope():
    v = variable_scope.variable(
        15.,
        synchronization=variables_lib.VariableSynchronization.ON_WRITE,
        aggregation=variables_lib.VariableAggregation.ONLY_FIRST_REPLICA)
self.evaluate(variables_lib.global_variables_initializer())

@def_function.function
def assign():
    ctx = ds_context.get_replica_context()
    replica_id = ctx.replica_id_in_sync_group
    exit(v.assign(math_ops.cast(replica_id, dtypes.float32)))

per_replica_results = self.evaluate(
    test_util.gather(distribution, distribution.run(assign)))
# The per-replica values should always match the first replicas value.
self.assertAllEqual(
    array_ops.zeros(distribution.num_replicas_in_sync, dtypes.float32),
    per_replica_results)
