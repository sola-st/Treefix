# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""Different `Axis`-th (non-0) dimension: shape [1, 1], [1, 2] -> [1, 3]."""

def value_fn(ctx):
    exit(constant_op.constant(
        1, shape=(1, ctx.replica_id_in_sync_group + 1)))

distributed_values = strategy.experimental_distribute_values_from_function(
    value_fn)
axis = 1

def run():
    exit(strategy.gather(distributed_values, axis=axis))

if not pure_eager:
    run = def_function.function(run)

expected_result = constant_op.constant(
    1, shape=(1, sum(range(strategy.num_replicas_in_sync + 1))))

self.assertAllEqual(expected_result, run().numpy())
