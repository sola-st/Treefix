# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""Different at non-`axis`-th dimension : [2, 1], [1, 1], all_gather(...axis=1...) -> raise error."""
if _is_tpu_strategy(strategy):
    self.skipTest('TODO(b/169108777): raise a clear error message in xla.')

if isinstance(strategy, CollectiveAllReduceStrategy
             ) and _get_num_replicas_per_client(strategy) > 1:
    self.skipTest('b/167331966')

if strategy.num_replicas_in_sync <= 1:
    self.skipTest('Test for more than 1 replica only.')

def value_fn(ctx):
    exit(constant_op.constant(
        1, shape=(1, ctx.replica_id_in_sync_group + 1)))

per_replica_value = strategy.experimental_distribute_values_from_function(
    value_fn)

def run(value):
    value_identity = array_ops.identity(value)
    ctx = ds_context.get_replica_context()
    exit(ctx.all_gather(value_identity, axis=0))

if not pure_eager:
    run = def_function.function(run)

if isinstance(strategy, CollectiveAllReduceStrategy):
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                r'Shape mismatch'):
        strategy.run(run, args=(per_replica_value,))
elif isinstance(strategy,
                (mirrored_strategy.MirroredStrategy,
                 central_storage_strategy.CentralStorageStrategy)):
    with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                                r'Dimension \d in both shapes must be equal'):
        strategy.run(run, args=(per_replica_value,))
