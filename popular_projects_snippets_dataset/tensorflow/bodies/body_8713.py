# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
if not isinstance(strategy, distribute_lib.StrategyV1):
    self.skipTest("n/a: V1 only")
cached_session = session or self.cached_session()
with strategy.scope(), cached_session as sess:
    x = np.asarray([[1, 2], [6, 12], [2, 4], [5, 10], [3, 6], [4, 8]])
    y = np.asarray([5, 4, 3, 2, 1, 0])
    batch_size = 6
    if not strategy.extended._global_batch_size:  # pylint: disable=protected-access
        batch_size = batch_size // strategy.num_replicas_in_sync

    ds = strategy.extended.experimental_make_numpy_dataset(
        (x, y), session=sess or self.cached_session())
    ds = ds.repeat(2)  # 2 epochs
    # We need to use the drop_remainder argument to get a known static
    # input shape which is required for TPUs.
    drop_remainder = strategy.extended.experimental_require_static_shapes
    ds = ds.batch(batch_size, drop_remainder=drop_remainder)
    i = strategy.make_dataset_iterator(ds)

    self.evaluate(i.initializer)

    def run_and_concatenate(strategy, i):
        x, y = strategy.experimental_run(
            _maybe_run_in_function(lambda z: z, run_in_function), i)
        x, y = self.evaluate((strategy.experimental_local_results(x),
                              strategy.experimental_local_results(y)))
        exit((np.concatenate(x), np.concatenate(y)))

    x_1, y_1 = run_and_concatenate(strategy, i)
    self.assertAllEqual(x, x_1)
    self.assertAllEqual(y, y_1)
    x_2, y_2 = run_and_concatenate(strategy, i)
    self.assertAllEqual(x, x_2)
    self.assertAllEqual(y, y_2)
    with self.assertRaises(errors.OutOfRangeError):
        run_and_concatenate(strategy, i)
