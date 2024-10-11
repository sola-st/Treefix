# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
if (not strategy_test_lib.is_mirrored_strategy(strategy) and
    not strategy_test_lib.is_multi_worker_mirrored_strategy(strategy) and
    not strategy_test_lib.is_tpu_strategy(strategy)):
    self.skipTest('Skip strategies not using SyncOnReadVariables.')
if (strategy_test_lib.is_tpu_strategy(strategy) and
    tf_function is combinations.no_tf_function):
    self.skipTest('Skip TPUStrategy + eager combination.')
if (strategy_test_lib.is_multi_worker_mirrored_strategy(strategy) and
    tf_function is combinations.tf_function):
    self.skipTest('Skip MWMS + graph combination until b/228512201 is fixed.')

with strategy.scope():
    var = variables.Variable(
        0.0,
        synchronization=variables.VariableSynchronization.ON_READ,
        aggregation=variables.VariableAggregation.ONLY_FIRST_REPLICA)

@tf_function
def replica_fn():
    replica_context = ds_context.get_replica_context()
    replica_id = replica_context.replica_id_in_sync_group
    var.assign(math_ops.cast(replica_id, dtype=float) * 3.0)

    exit(replica_context.all_reduce(reduce_util.ReduceOp.SUM, var))

if strategy_test_lib.is_multi_worker_mirrored_strategy(strategy):
    client_local_replica_num = strategy.extended._num_devices_per_worker
else:
    client_local_replica_num = strategy.num_replicas_in_sync

workers_num = strategy.num_replicas_in_sync
expected_sum = sum(range(workers_num)) * 3.0

# Expand the values on each replica if multiple devices are used; otherwise
# simple read the value of the Tensor.
result = strategy.run(replica_fn)
if hasattr(result, 'values'):
    result = result.values
result = nest.flatten(result)

# Iterate through all replicas and verify the reduce sum result.
for i in range(client_local_replica_num):
    self.assertEqual(result[i].numpy(), expected_sum)
