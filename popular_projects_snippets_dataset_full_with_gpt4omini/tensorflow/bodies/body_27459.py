# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset1 = dataset_ops.Dataset.list_files(
    self._filenames, shuffle=False)
dataset1 = dataset1.apply(
    interleave_ops.parallel_interleave(core_readers.TFRecordDataset, 10))
dataset2 = dataset_ops.Dataset.list_files(
    self._filenames, shuffle=False)
dataset2 = dataset2.apply(
    interleave_ops.parallel_interleave(core_readers.TFRecordDataset, 10))

dataset = dataset_ops.Dataset.zip((dataset1, dataset2))
dataset = distribute._AutoShardDataset(dataset, 5, 3)

expected = [
    (b"Record %d of file %d" % (r, f), b"Record %d of file %d" % (r, f))  # pylint:disable=g-complex-comprehension
    for r in range(0, 10)
    for f in (3, 8)
]

self.assertDatasetProduces(dataset, expected)
