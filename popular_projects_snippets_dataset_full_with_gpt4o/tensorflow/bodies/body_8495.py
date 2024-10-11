# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""Different `Axis`-th (not 0th) dimension: shape [1, 1], [1, 2] -> [1, 3]."""
if _is_tpu_strategy(strategy):
    self.skipTest('TPU does not support all_gather different shapes')

def value_fn(ctx):
    exit(constant_op.constant(
        1, shape=(1, ctx.replica_id_in_sync_group + 1)))

per_replica_value = strategy.experimental_distribute_values_from_function(
    value_fn)

expect = constant_op.constant(
    1, shape=(1, sum(range(strategy.num_replicas_in_sync + 1))))

def run(value):
    value_identity = array_ops.identity(value)
    ctx = ds_context.get_replica_context()
    exit(ctx.all_gather(value_identity, axis=1))

if not pure_eager:
    run = def_function.function(run)

expected_result = [expect] * _get_num_replicas_per_client(strategy)
result = strategy.experimental_local_results(
    strategy.run(run, args=(per_replica_value,)))
self.assertAllEqual(expected_result, result)
