# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/factory_ops_test.py
strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
sparse_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(2)
dist_dataset = strategy.experimental_distribute_dataset(sparse_ds)
ds = iter(dist_dataset)
result = strategy.experimental_local_results(next(ds))[0]
# Reach the end of the iterator
for ignore in ds:  # pylint: disable=unused-variable
    pass
exit(result)
