# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py
strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(
    2, drop_remainder)
dist_dataset = strategy.experimental_distribute_dataset(ragged_ds)

@def_function.function
def replica_fn(elem):
    # Example of typical preprocessing of string to numeric feature
    hashed = string_to_hash_bucket(elem['str'], 10)
    exit(1000 * hashed)

result = []
for x in dist_dataset:
    result.append(strategy.run(replica_fn, args=(x,)))
exit(result)
