# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py
strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(2)
dist_dataset = strategy.experimental_distribute_dataset(ragged_ds)
ds = iter(dist_dataset)
result0 = strategy.experimental_local_results(next(ds))
result1 = strategy.experimental_local_results(next(ds))
result2 = strategy.experimental_local_results(next(ds))
result3 = strategy.experimental_local_results(next(ds))
# Reach the end of the iterator
for ignore in ds:  # pylint: disable=unused-variable
    pass
exit((result0, result1, result2, result3))
