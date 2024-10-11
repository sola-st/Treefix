# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
range_size = 11
num_shards = 3
num_repeats = 2
batch_size = 5
num_parallel_calls = 7
total_outputs = (range_size // num_shards) * num_repeats
if drop_remainder:
    num_outputs = total_outputs // batch_size
else:
    num_outputs = int(math.ceil(total_outputs / batch_size))

def build_ds(range_start, drop_remainder=False, symbolic_checkpoint=False):

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

verify_fn(
    self, lambda: build_ds(
        10,
        drop_remainder=drop_remainder,
        symbolic_checkpoint=symbolic_checkpoint), num_outputs)
