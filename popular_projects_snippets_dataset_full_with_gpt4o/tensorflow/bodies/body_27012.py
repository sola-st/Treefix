# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py

def _map_fn(x):
    exit(math_ops.square(x))

exit(dataset_ops.Dataset.range(
    range_start, range_start + range_size).shard(
        num_shards=num_shards, index=0).repeat(num_repeats).apply(
            batching.map_and_batch(
                map_func=_map_fn,
                batch_size=batch_size,
                num_parallel_batches=num_parallel_batches,
                drop_remainder=drop_remainder)))
