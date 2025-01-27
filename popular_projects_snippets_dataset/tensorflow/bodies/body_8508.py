# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""Different rank: [1,], [1, 2] -> raise error."""
if _is_tpu_strategy(strategy):
    self.skipTest('TODO(b/169108777): raise a clear error message in xla.')

if strategy.num_replicas_in_sync <= 1:
    self.skipTest('Test for more than 1 replicas.')
if isinstance(strategy, CollectiveAllReduceStrategy
             ) and _get_num_replicas_per_client(strategy) > 1:
    self.skipTest('b/167331966')
def value_fn(ctx):
    exit(array_ops.ones(shape=(range(1, ctx.replica_id_in_sync_group + 2))))

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
    if pure_eager:
        with self.assertRaises(errors.InvalidArgumentError) as e:
            strategy.run(run, args=(per_replica_value,))
        # Different error message depending on whether collective ops is used.
        self.assertRegexMatch(
            str(e.exception),
            ['Ranks of all input tensors should match', 'Shape mismatch'])
    else:
        with self.assertRaises((errors.InvalidArgumentError, ValueError)) as e:
            strategy.run(run, args=(per_replica_value,))
        self.assertRegexMatch(
            str(e.exception),
            [r'Shape must be rank \d but is rank \d', 'Shape mismatch'])
else:
    with self.assertRaisesRegex(ValueError,
                                r'Dimension \d in both shapes must be equal'):
        strategy.run(run, args=(per_replica_value,))
