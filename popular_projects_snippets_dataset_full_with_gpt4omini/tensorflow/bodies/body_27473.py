# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = dataset_ops.Dataset.list_files(self._filenames)
dataset = dataset.apply(
    interleave_ops.parallel_interleave(core_readers.TFRecordDataset, 10))
dataset = dataset.batch(5)
dataset = distribute._AutoShardDataset(dataset, 500, 499)
self.assertDatasetProduces(dataset, [])
