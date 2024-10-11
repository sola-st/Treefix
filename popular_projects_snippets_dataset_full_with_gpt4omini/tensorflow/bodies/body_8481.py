# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
per_replica_value = strategy.experimental_distribute_values_from_function(
    lambda _: array_ops.identity(value_on_replica))

def replica_fn(per_replica_value):
    ctx = ds_context.get_replica_context()
    local_value = array_ops.identity(per_replica_value)
    exit(ctx.all_gather(local_value, axis=axis))

if not pure_eager:
    replica_fn = def_function.function(replica_fn)

result = strategy.experimental_local_results(
    strategy.run(replica_fn, args=(per_replica_value,)))

all_value = [value_on_replica for _ in range(strategy.num_replicas_in_sync)]
expect = array_ops.concat(all_value, axis=axis)
expected_result = [expect] * _get_num_replicas_per_client(strategy)

self.assertAllClose(expected_result, result)
