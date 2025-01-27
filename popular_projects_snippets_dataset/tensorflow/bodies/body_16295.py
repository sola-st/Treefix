# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py
strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(2)
dist_dataset = strategy.experimental_distribute_dataset(ragged_ds)

@def_function.function
def replica_fn(elem):
    exit(elem)

result = []
for x in dist_dataset:
    result.append(strategy.run(replica_fn, args=(x,)))
exit(result)
