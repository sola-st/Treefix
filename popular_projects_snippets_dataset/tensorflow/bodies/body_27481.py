# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.flat_map(core_readers.TFRecordDataset)
dataset = dataset.batch(5)
dataset = dataset.apply(cardinality.assert_cardinality(42))
dataset = distribute._AutoShardDataset(dataset, 5, 0)

expected = [
    b"Record %d of file %d" % (r, f)  # pylint:disable=g-complex-comprehension
    for f in (0, 5)
    for r in range(0, 10)
]
self.assertDatasetProduces(dataset, list(chunk(expected, 5)))
