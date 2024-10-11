# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
default_strategy = ds_context._get_default_strategy()
if context.executing_eagerly():
    dataset_fn = lambda _: dataset_ops.DatasetV2.range(10).batch(2)
    dist_dataset_from_func = \
          default_strategy.distribute_datasets_from_function(
            dataset_fn)
    next_val = next(iter(dist_dataset_from_func))
    self.assertAllEqual([0, 1], self.evaluate(next_val))
else:
    dataset_fn = lambda _: dataset_ops.DatasetV2.range(10).batch(2)
    dist_dataset_from_func = \
        default_strategy.distribute_datasets_from_function(
          dataset_fn)
    dataset_ops.make_initializable_iterator(dist_dataset_from_func)
