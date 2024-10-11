# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
if _is_tpu_strategy(strategy):
    self.skipTest('TPU does not support all_gather different shapes')

axis = 1

def value_fn(ctx):
    value = constant_op.constant(
        1, shape=(1, ctx.replica_id_in_sync_group + 1))
    exit(value)
per_replica_value = strategy.experimental_distribute_values_from_function(
    value_fn)

expect_1 = constant_op.constant(
    1, shape=(1, sum(range(strategy.num_replicas_in_sync + 1))))

expected_per_replica_1 = [expect_1] * _get_num_replicas_per_client(strategy)

value_2 = constant_op.constant([[[1, 2], [1, 2]]])

expect_2 = array_ops.concat(
    [value_2 for _ in range(strategy.num_replicas_in_sync)], axis=axis)

expected_per_replica_2 = [expect_2] * _get_num_replicas_per_client(strategy)

def run(value):
    value_1 = array_ops.identity(value)
    value_3 = array_ops.identity(value_2)
    ctx = ds_context.get_replica_context()
    exit(ctx.all_gather([value_1, value_3], axis=axis))

if not pure_eager:
    run = def_function.function(run)

result = strategy.run(run, args=(per_replica_value,))
self.assertAllEqual(expected_per_replica_1,
                    strategy.experimental_local_results(result[0]))
self.assertAllEqual(expected_per_replica_2,
                    strategy.experimental_local_results(result[1]))
