# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = core_readers.TFRecordDataset(self._filenames)
dataset = distribute._AutoShardDataset(dataset, 5, 0)

expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in (0, 5)
    for r in range(0, 10)
]
self.assertDatasetProduces(dataset, expected)
