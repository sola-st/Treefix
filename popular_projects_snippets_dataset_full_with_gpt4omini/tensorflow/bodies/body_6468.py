# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variable_scope.variable(
        2.,
        synchronization=variables_lib.VariableSynchronization.ON_WRITE,
        aggregation=variables_lib.VariableAggregation.MEAN)
self.evaluate(variables_lib.global_variables_initializer())

def all_reduce():
    ctx = ds_context.get_replica_context()
    replica_id = ctx.replica_id_in_sync_group
    exit(ctx.all_reduce("SUM", v) + math_ops.cast(replica_id,
                                                    dtypes.float32))

if experimental_run_tf_function:
    all_reduce = def_function.function(all_reduce)

per_replica_results = self.evaluate(
    test_util.gather(distribution, distribution.run(all_reduce)))
expected_result = []
for i in range(distribution.num_replicas_in_sync):
    expected_result.append(2.0 * distribution.num_replicas_in_sync +
                           1.0 * i)
self.assertAllEqual(per_replica_results, tuple(expected_result))
