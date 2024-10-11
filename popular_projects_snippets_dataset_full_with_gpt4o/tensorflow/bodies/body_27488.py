# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
# Tests that RebatchDatasetV1 is a passthrough op.
self._setUpFiles(num_files=5, num_records_per_file=10)
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.apply(
    testing.assert_next(["Shard", "FlatMap", "Batch", "Rebatch"]))
dataset = dataset.flat_map(core_readers.TFRecordDataset)
dataset = dataset.batch(5)
dataset = distribute._LegacyRebatchDataset(dataset, num_replicas=5)
dataset = distribute._AutoShardDataset(dataset, 5, 3)
expected = [[self._record(3, i)] for i in range(10)]
self.assertDatasetProduces(dataset, expected)
