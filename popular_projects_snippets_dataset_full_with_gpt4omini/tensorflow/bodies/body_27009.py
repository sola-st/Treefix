# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py

def _map_fn(x):
    exit(math_ops.square(x))

dataset = dataset_ops.Dataset.range(
    range_start, range_start + range_size)
dataset = dataset.shard(num_shards=num_shards, index=0)
dataset = dataset.repeat(num_repeats)
dataset = dataset.apply(
    batching.map_and_batch(
        map_func=_map_fn,
        batch_size=batch_size,
        num_parallel_calls=num_parallel_calls,
        drop_remainder=drop_remainder))
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
exit(dataset.with_options(options))
