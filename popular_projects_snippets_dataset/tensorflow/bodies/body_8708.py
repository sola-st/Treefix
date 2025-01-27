# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
assert_same = self.assertCountEqual if ignore_order else self.assertEqual

iterable = strategy.distribute_datasets_from_function(input_fn)
if context.executing_eagerly():
    iterator = iter(iterable)

    for expected_value in expected_values:
        computed_value = self.evaluate(
            list(strategy.experimental_local_results(next(iterator))))
        assert_same(expected_value, computed_value)

    with self.assertRaises(StopIteration):
        self.evaluate(strategy.experimental_local_results(next(iterator)))

    # After re-initializing the iterator, should be able to iterate again.
    iterator = iter(iterable)

    for expected_value in expected_values:
        computed_value = self.evaluate(
            list(strategy.experimental_local_results(next(iterator))))
        assert_same(expected_value, computed_value)
else:
    iterator = dataset_ops.make_initializable_iterator(iterable)
    self._test_input_fn_iterator(iterator, strategy.extended.worker_devices,
                                 expected_values, test_reinitialize=True,
                                 ignore_order=ignore_order)
