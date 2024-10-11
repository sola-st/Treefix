# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.apply(
    interleave_ops.parallel_interleave(core_readers.TFRecordDataset, 10))
dataset = dataset.map(lambda x: string_ops.substr_v2(x, 2, 1000))
dataset = dataset.batch(5)
dataset = distribute._AutoShardDataset(dataset, 5, 3)

expected = [
    b"cord %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for r in range(0, 10)
    for f in (3, 8)
]
self.assertDatasetProducesWithShuffle(dataset, expected, 5, 4, shuffle)
