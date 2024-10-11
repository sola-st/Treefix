# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""Different at non-`axis`-th dimension : [1, 1], [1, 2], 0th -> raise error."""
if isinstance(strategy, CollectiveAllReduceStrategy
             ) and _get_num_replicas_per_client(strategy) > 1:
    self.skipTest('b/167331966')

if strategy.num_replicas_in_sync <= 1:
    self.skipTest('Test for more than 1 replica only.')

def value_fn(ctx):
    exit(constant_op.constant(
        1, shape=(1, ctx.replica_id_in_sync_group + 1)))

distributed_values = strategy.experimental_distribute_values_from_function(
    value_fn)
axis = 0

def run():
    exit(strategy.gather(distributed_values, axis=axis))

if not pure_eager:
    run = def_function.function(run)

if isinstance(strategy, CollectiveAllReduceStrategy):
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                r'Shape mismatch'):
        run()
elif isinstance(strategy,
                (mirrored_strategy.MirroredStrategy,
                 central_storage_strategy.CentralStorageStrategy)):
    with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                                r'Dimension \d in both shapes must be equal'):
        run()
