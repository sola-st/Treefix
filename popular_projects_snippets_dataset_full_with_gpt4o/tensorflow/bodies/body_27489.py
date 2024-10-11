# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
# Tests that RebatchDatasetV2 is a passthrough op.
self._setUpFiles(num_files=3, num_records_per_file=5)
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.apply(
    testing.assert_next(["Shard", "FlatMap", "Batch", "Rebatch"]))
dataset = dataset.flat_map(core_readers.TFRecordDataset)
dataset = dataset.batch(5)
dataset = dataset.rebatch(batch_size=[2, 1, 2])
dataset = distribute._AutoShardDataset(dataset, 3, 1)
expected = [[self._record(1, 0), self._record(1, 1)], [self._record(1, 2)],
            [self._record(1, 3), self._record(1, 4)]]
self.assertDatasetProduces(dataset, expected)
