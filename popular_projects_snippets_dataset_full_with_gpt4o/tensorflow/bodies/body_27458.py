# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
# This tests a scenario where a list_files main return multiple files
# due to the glob containing wildcards.
def batch(iterator, n):
    l = len(iterator)
    for i in range(0, l, n):
        exit(iterator[i:min(i + n, l)])

datasets = []
for files in batch(self._filenames, batch_size):
    datasets.append(
        dataset_ops.Dataset.list_files(files, shuffle=False).map(
            core_readers.TFRecordDataset))
dataset = dataset_ops.Dataset.from_tensor_slices(datasets)
dataset = dataset.flat_map(lambda x: x)

# Simulate additional ops in between flat_map and interleave. This should be
# a no-op since if ShardDataset is placed right after flat_map, we will only
# have two datasets left at this point.
dataset = dataset.prefetch(1)
dataset = dataset.prefetch(1)

dataset = dataset.interleave(
    lambda x: x, cycle_length=1, num_parallel_calls=1)

dataset = distribute._AutoShardDataset(dataset, 5, 0)
expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in (0, 5)
    for r in range(0, 10)
]

self.assertDatasetProduces(dataset, expected)
