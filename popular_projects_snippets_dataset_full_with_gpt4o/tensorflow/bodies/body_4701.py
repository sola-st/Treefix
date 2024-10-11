# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
default_strategy = ds_context._get_default_strategy()
if context.executing_eagerly():
    dataset_fn = lambda _: dataset_ops.DatasetV2.range(10).batch(2)
    dist_dataset = default_strategy.experimental_distribute_dataset(
        dataset_fn(distribute_lib.InputContext()))
    next_val = next(iter(dist_dataset))
else:
    dataset_fn = lambda _: dataset_ops.DatasetV1.range(10).batch(2)
    dist_dataset = default_strategy.experimental_distribute_dataset(
        dataset_fn(distribute_lib.InputContext()))
    iterator = dist_dataset.make_initializable_iterator()
    self.evaluate(iterator.initializer)
    next_val = iterator.get_next()
self.assertAllEqual([0, 1], self.evaluate(next_val))
