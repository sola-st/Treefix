# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset1 = dataset_ops.Dataset.list_files(
    self._filenames, shuffle=shuffle)
dataset1 = dataset1.apply(
    interleave_ops.parallel_interleave(core_readers.TFRecordDataset, 10))
dataset1 = dataset1.batch(5)
dataset2 = dataset_ops.Dataset.list_files(
    self._filenames, shuffle=shuffle)
dataset2 = dataset2.apply(
    interleave_ops.parallel_interleave(core_readers.TFRecordDataset, 10))
dataset2 = dataset2.batch(5)

dataset = dataset1.concatenate(dataset2)
dataset = distribute._AutoShardDataset(dataset, 5, 3)

expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for r in range(0, 10)
    for f in (3, 8)
]
expected += expected
self.assertDatasetProducesWithShuffle(dataset, expected, 5, 8, shuffle)
