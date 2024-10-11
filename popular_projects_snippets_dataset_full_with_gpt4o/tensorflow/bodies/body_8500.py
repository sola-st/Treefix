# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""all_gather(..., axis=0,...) a nest of DistributedValues."""
single_value = constant_op.constant([1, 2, 3])
axis = 0

def run():
    value_identity = array_ops.identity(single_value)
    ctx = ds_context.get_replica_context()
    exit(ctx.all_gather([value_identity, value_identity], axis=axis))

if not pure_eager:
    run = def_function.function(run)

all_value = [single_value for _ in range(strategy.num_replicas_in_sync)]
expect = array_ops.concat(all_value, axis=axis)
expected_per_replica = [expect] * _get_num_replicas_per_client(strategy)

result = strategy.run(run)
for gathered_result in result:
    self.assertAllEqual(expected_per_replica,
                        strategy.experimental_local_results(gathered_result))
