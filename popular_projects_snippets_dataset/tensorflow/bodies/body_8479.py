# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
"""Different rank: [1,], [1, 2] -> raise error."""
if strategy.num_replicas_in_sync <= 1:
    self.skipTest('Test for more than 1 replicas.')
if isinstance(strategy, CollectiveAllReduceStrategy
             ) and _get_num_replicas_per_client(strategy) > 1:
    self.skipTest('b/167331966')
def value_fn(ctx):
    exit(array_ops.ones(shape=(range(1, ctx.replica_id_in_sync_group + 2))))

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
elif isinstance(
    strategy,
    (mirrored_strategy.MirroredStrategy,
     central_storage_strategy.CentralStorageStrategy)):
    if pure_eager:
        with self.assertRaises(errors.InvalidArgumentError) as e:
            run()
        # Different error message depending on whether collective ops is used.
        self.assertRegexMatch(
            str(e.exception),
            ['Ranks of all input tensors should match', 'Shape mismatch'])
    else:
        with self.assertRaises((errors.InvalidArgumentError, ValueError)) as e:
            run()
        self.assertRegexMatch(
            str(e.exception),
            [r'Shape must be rank \d but is rank \d', 'Shape mismatch'])
elif _is_tpu_strategy(strategy) and pure_eager:
    with self.assertRaisesRegex(ValueError,
                                r'Dimension \d in both shapes must be equal'):
        run()
else:
    with self.assertRaisesRegex(ValueError,
                                r'Shape must be rank \d but is rank \d'):
        run()
