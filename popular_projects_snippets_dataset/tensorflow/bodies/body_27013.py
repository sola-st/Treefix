# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
range_size = 11
num_shards = 3
num_repeats = 2
batch_size = 5
num_parallel_batches = 2
total_outputs = (range_size // num_shards) * num_repeats
if drop_remainder:
    num_outputs = total_outputs // batch_size
else:
    num_outputs = int(math.ceil(total_outputs / batch_size))

def build_ds(range_start, drop_remainder):

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

verify_fn(self, lambda: build_ds(10, drop_remainder=drop_remainder),
          num_outputs)
